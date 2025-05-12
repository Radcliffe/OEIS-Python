import os
import re
import sys

from read_oeis import OEISReader, OEISWriter

def fix_indentation(filepath):
    """
    Fix the indentation of the OEIS file.
    """
    reader = OEISReader(filepath)
    reader.read_file()
    lines = reader.lines
    changed = False
    for i, line in enumerate(lines):
        if line.language == 'Python':
            match = re.match(r"^(\.+)(.*)$", line.content)
            if match:
                line.content = ' ' * len(match.group(1)) + match.group(2)
                changed = True
    if changed:
        fixed_filepath = filepath.replace(".seq", "_indent_fixed.seq")
        writer = OEISWriter(fixed_filepath)
        writer.write_lines(lines)
        sequence_id = lines[0].sequence_id
        print(sequence_id)


def fix_indentation_in_directory(directory):
    """
    Fix the indentation of all OEIS files in the directory.
    """
    # Walk through the directory and fix indentation for each file
    for root, _, files in sorted(os.walk(directory)):
        for file in files:
            if file.endswith(".seq"):
                filepath = os.path.join(root, file)
                fix_indentation(filepath)


if __name__ == "__main__":
    # Define the OEIS data directory
    oeis_data_dir = "../oeisdata/seq"
    # Fix indentation for all OEIS files in the directory
    fix_indentation_in_directory(oeis_data_dir)