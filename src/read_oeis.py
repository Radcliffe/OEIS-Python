import re
from typing import List, Optional
import requests_cache

from models.oeis_models import OEISLine, OEISLineType

session = requests_cache.CachedSession('demo_cache')


def get_language(content, language):
    match = re.search(r"^\((.*?)\)", content)
    if match is None:
        return language
    new_language = match.group(1).strip()
    if new_language == '': return language
    whitelist = ['bash', 'bc', 'ksh', 'mzscheme', 'nauty', 'newLISP', 'perl/tcsh', 'plantri', 'zsh']
    if (new_language < 'A' or new_language[0] > 'Z') and not new_language in whitelist:
        return language
    if re.search(r'[aA]\d{6}', new_language): return language
    if new_language.startswith('Python'):
        new_language = 'Python'
    if new_language not in languages_seen:
        languages_seen.add(new_language)
    return new_language

languages_seen = set()

class OEISReader:
    """
    A class to read and parse the OEIS file.
    """
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.lines: List[OEISLine] = []
        self.sequence_id: Optional[str] = None
        self.name: Optional[str] = None

    def read_file(self):
        language = None
        with open(self.file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                language = self.parse_line(line, language)

    def parse_line(self, line: str, language: Optional[str]) -> Optional[str]:
        parts = line.split(' ', maxsplit=2)
        if len(parts) < 3:
            return language
        line_type, sequence_id, content = parts
        line_type = OEISLineType(line_type)
        if line_type == OEISLineType.NAME:
            if self.name is not None:
                raise ValueError(f"Duplicate name line for sequence {self.sequence_id}")
            self.name = content.strip()
            return language
        if self.sequence_id is None:
            self.sequence_id = sequence_id
        elif self.sequence_id != sequence_id:
            raise ValueError(f"Unexpected sequence ID: {sequence_id}. Expected: {self.sequence_id}")
        if line_type == OEISLineType.MATHEMATICA_PROGRAM:
            language = "Mathematica"
        elif line_type == OEISLineType.MAPLE_PROGRAM:
            language = "Maple"
        elif line_type == OEISLineType.OTHER_PROGRAM:
            language = get_language(content, language)

        else:
            language = None
        oeis_line = OEISLine(line_type=line_type, sequence_id=sequence_id, content=content, language=language)
        self.lines.append(oeis_line)
        return language

    def get_data(self) -> List[int]:
        """
        Extracts the sequence data from the lines. (Line types %S, %T, %U)
        """
        data = []
        for line in self.lines:
            if line.line_type in {OEISLineType.SEQUENCE, OEISLineType.SECOND_LINE, OEISLineType.THIRD_LINE}:
                numbers = re.findall(r'-?\d+', line.content)
                data.extend(int(num) for num in numbers)
        return data

    def get_offset(self) -> int:
        """
        Extracts the offset from the lines. (Line type %O)
        """
        for line in self.lines:
            if line.line_type == OEISLineType.OFFSET:
                match = re.search(r'(\d+)', line.content)
                if match:
                    return int(match.group(1))
        return 0

    def get_bfile(self):
        """
        Fetches the bfile data if it exists for the sequence.
        The link eo the bfile looks like:
        %H A034874 Reinhard Zumkeller, <a href="/A034874/b034874.txt">Table of n, a(n) for n = 1..250</a>
        :return: The bfile data as a list of integers or None if not found.
        """
        target = f"<a href=\"/{self.sequence_id}/b"
        for line in self.lines:
            if line.line_type == OEISLineType.LINK and target in line.content:
                match = re.search(r'href="/(\w+)/b(\w+).txt"', line.content)
                if match:
                    sequence_id = match.group(1)
                    file_name = match.group(2)
                    url = f"https://oeis.org/{sequence_id}/b{file_name}.txt"
                    response = session.get(url)
                    if response.status_code == 200:
                        lines = [line for line in response.text.splitlines()
                                 if line.strip() and not line.startswith('#')]
                        return [int(x) for x in ' '.join(lines).split()[1::2]]
        return None


class OEISWriter:
    """
    A class to write OEIS lines to a file.
    """
    def __init__(self, file_path: str):
        self.file_path = file_path

    def write_lines(self, lines: List[OEISLine]):
        with open(self.file_path, 'w') as file:
            for line in lines:
                file.write(f"{line.line_type.value} {line.sequence_id} {line.content}\n")

def test_oeis_reader():
    oeis_reader = OEISReader("../oeisdata/seq/A003/A003586.seq")
    oeis_reader.read_file()
    for line in oeis_reader.lines:
        print(line.language, line, sep=' | ')
    data = oeis_reader.get_data()
    print("Extracted data:", data)
    offset = oeis_reader.get_offset()
    print("Extracted offset:", offset)
    bfile_data = oeis_reader.get_bfile()
    if bfile_data:
        print("Bfile data:", bfile_data[:10], "...")  # Print first 10 elements for brevity
    else:
        print("No bfile data found.")


if __name__ == "__main__":
    test_oeis_reader()