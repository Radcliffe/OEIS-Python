import os
import re
import sys
import csv # Import the csv module

# CORRECTED Regex: Finds '/' only when it's NOT part of '//'
# (?<!/) : Negative lookbehind - asserts the preceding char is NOT '/'
# /      : Match a literal forward slash
# (?!/)  : Negative lookahead - asserts the following char is NOT '/'
pattern = re.compile(r"(?<!/)/(?!/)")


def find_potential_division(directory, output_csv_file):
    """
    Recursively searches for .py files in the given directory (alphabetically),
    identifies lines containing single forward slashes used for division ('/'
    but not '//'), and writes the findings to a CSV file.

    Args:
        directory (str): The path to the directory to search.
        output_csv_file (str): The path to the CSV file to write results to.
    """
    if not os.path.isdir(directory):
        print(f"Error: Directory not found: {directory}")
        sys.exit(1)

    print(f"Searching for potential division '/' (not '//') in: {directory}")
    print(f"Results will be saved to: {output_csv_file}")
    print("-" * 60)

    found_count = 0
    processed_files = 0
    results = []

    for dirpath, dirnames, filenames in os.walk(directory, topdown=True):
        dirnames.sort()
        filenames.sort()

        for filename in filenames:
            if filename.lower().endswith(".py"):
                filepath = os.path.join(dirpath, filename)
                processed_files += 1
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        for _ in range(4):
                            next(f, None)
                        for line_num, line in enumerate(f, 1):
                            if pattern.search(line):
                                comment_index = line.find('#')
                                search_part = line if comment_index == -1 else line[:comment_index]

                                if pattern.search(search_part):
                                    stem = os.path.splitext(filename)[0]
                                    if '_' in stem:
                                        sequence, index = stem.split("_")
                                    else:
                                        sequence, index = stem, 1
                                    url = f"https://oeis.org/{sequence}"
                                    results.append([sequence, url, index, line_num, line.rstrip(), 'Review'])
                                    found_count += 1

                except (IOError, OSError) as e:
                    print(f"Warning: Error reading file {filepath}: {e}")
                except Exception as e:
                    print(f"Warning: Unexpected error processing file {filepath}: {e}")

    print("-" * 60)
    print("Search complete.")
    print(f"Processed {processed_files} Python files.")
    print(f"Found {found_count} potential instance(s).")
    return results


def write_csv(output_csv_file, results):
    """
    Write the results to a CSV file.

    Args:
        output_csv_file (str): The path to the CSV file to write results to.
        results (list): A list of rows to write to the CSV file.
    """
    try:
        with open(output_csv_file, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            # Write the header row
            csv_writer.writerow(["Sequence", "Url", "Index", "Line number", "Line", "Status"])
            # Write the data rows
            csv_writer.writerows(results)
        print(f"Results saved to {output_csv_file}")
    except (IOError, OSError) as e:
        print(f"Fatal Error: Could not open or write to output CSV file {output_csv_file}: {e}")
        sys.exit(1)
    except csv.Error as e:
        print(f"Fatal Error: CSV writing error in {output_csv_file}: {e}")
        sys.exit(1)


# Write to excel file with columns "Sequence", "Index", "Line number", "Line", "Status"
# The sequence should have a link to the OEIS page
def write_excel(output_excel_file, results):
    """
    Write the results to an Excel file.

    Args:
        output_excel_file (str): The path to the Excel file to write results to.
        results (list): A list of rows to write to the Excel file.
    """
    import pandas as pd
    df = pd.DataFrame(results, columns=["Sequence", "Url", "Index", "Line number", "Line", "Status"])
    df.drop(columns=["Url"], inplace=True)
    df["Index"] = df["Index"].astype(int)
    df["Line number"] = df["Line number"].astype(int)
    df.to_excel(output_excel_file, index=False)
    print(f"Results saved to {output_excel_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        script_name = os.path.basename(sys.argv[0])
        print("Usage: python {} <directory_to_search>".format(script_name))
        sys.exit(1)

    search_directory = sys.argv[1]
    # Define the output CSV filename (you could make this a command-line argument too)
    output_file = "division_report.csv"
    results = find_potential_division(search_directory, output_file)
    write_csv(output_file, results)
    write_excel(output_file.replace('.csv', '.xlsx'), results)
