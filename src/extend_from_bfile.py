from pathlib import Path

from walk_oeis import walk_oeis_sequences

oeis_data_dir = Path("../oeisdata/seq")


def main(oeis_data_dir: Path):
    """
    Find sequences that can be extended from their bfile data.
    """
    for reader in walk_oeis_sequences(oeis_data_dir):
        data = reader.get_data()
        data_str = ', '.join(map(str, data))
        if len(data_str) >= 150:
            continue
        try:
            bfile_data = reader.get_bfile()
        except ValueError:
            print(f"Error reading bfile for sequence {reader.current_sequence_id}. Skipping.")
            print("-" * 80)
            continue
        if bfile_data is None:
            continue
        if len(bfile_data) < len(data):
            print(f"bfile data is shorter than sequence data for {reader.current_sequence_id}. Skipping.")
            print("-" * 80)
            continue
        if bfile_data[:len(data)] != data:
            print(f"bfile data does not match sequence data for {reader.current_sequence_id}. Skipping.")
            print(f"Current data: {data_str}")
            print(f"Bfile data: {', '.join(map(str, bfile_data[:len(data)]))}")
            print("-" * 80)
            continue
        new_data_str = data_str
        for new_value in bfile_data[len(data):]:
            if abs(new_value) >= 10**60:
                break
            if len(new_data_str) + len(str(new_value)) + 2 > 260:
                break
            new_data_str += f", {new_value}"
        if new_data_str != data_str:
            print(f"Extend sequence {reader.current_sequence_id}")
            print(f"Current data: {data_str}")
            print(f"Extended data: {new_data_str}")
            print(f"Link: https://oeis.org/{reader.current_sequence_id}")
            print("-" * 80)

if __name__ == "__main__":
    main(oeis_data_dir)