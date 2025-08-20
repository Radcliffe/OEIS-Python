"""
Read and parse each sequence from the directory ../oeisdata/seq
"""

import os
from pathlib import Path
from read_oeis import OEISReader

def walk_oeis_sequences(oeis_data_dir: Path):
    """
    Walk through the OEIS data directory and yield each sequence file.

    Args:
        oeis_data_dir (Path): Path to the OEIS data directory.

    """
    for root, _, files in sorted(os.walk(oeis_data_dir)):
        for file in sorted(files):
            if file.endswith(".seq"):
                file_path = Path(root) / file
                # Read and parse the sequence file
                reader = OEISReader(file_path)
                reader.read_file()
                yield reader


def test_walk_oeis_sequences(oeis_data_dir: Path):
    """
    Test the walk_oeis_sequences function.
    """
    for reader in walk_oeis_sequences(oeis_data_dir):
        print(f"Sequence ID: {reader.current_sequence_id}")
        for line in reader.lines:
            print(f"{line.line_type}: {line.content}")
        print("-" * 40)


if __name__ == "__main__":
    # Define the OEIS data directory
    oeis_data_dir = Path("../oeisdata/seq")
    # Test the walk_oeis_sequences function
    test_walk_oeis_sequences(oeis_data_dir)