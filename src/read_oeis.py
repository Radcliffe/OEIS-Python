import re
from typing import List, Optional

from models.oeis_models import OEISLine, OEISLineType


class OEISReader:
    """
    A class to read and parse the OEIS file.
    """
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.lines: List[OEISLine] = []
        self.current_sequence_id: Optional[str] = None

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
        if self.current_sequence_id is None:
            self.current_sequence_id = sequence_id
        elif self.current_sequence_id != sequence_id:
            raise ValueError(f"Unexpected sequence ID: {sequence_id}. Expected: {self.current_sequence_id}")
        if line_type == OEISLineType.MATHEMATICA_PROGRAM:
            language = "Mathematica"
        elif line_type == OEISLineType.MAPLE_PROGRAM:
            language = "Maple"
        elif line_type == OEISLineType.OTHER_PROGRAM:
            if match := re.search(r"^\((.*?)\)", content):
                language = match.group(1)
        else:
            language = None
        oeis_line = OEISLine(line_type=line_type, sequence_id=sequence_id, content=content, language=language)
        self.lines.append(oeis_line)
        return language


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
    oeis_reader = OEISReader("../oeisdata/seq/A034/A034874.seq")
    oeis_reader.read_file()
    for line in oeis_reader.lines:
        print(line.language, line, sep=' | ')


if __name__ == "__main__":
    test_oeis_reader()