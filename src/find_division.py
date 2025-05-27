import os
import re
import sys

# CORRECTED Regex:
# (?<!/) : Negative lookbehind - asserts the preceding char is NOT '/'
# /      : Match a literal forward slash
# (?!/)  : Negative lookahead - asserts the following char is NOT '/'
# This finds '/' only when it's NOT part of '//'
pattern = re.compile(r"(?<!/)/(?!/)")

def find_potential_division(directory):
    """
    Recursively searches for .py files in the given directory and identifies
    lines containing single forward slashes used for division (i.e., '/'
    but not '//'), indicative of potential Python 2.7 integer division
    issues when moving to Python 3.

    Args:
        directory (str): The path to the directory to search.
    """
    if not os.path.isdir(directory):
        print("Error: Directory not found: {}".format(directory))
        sys.exit(1) # Exit if the directory doesn't exist

    print("Searching for potential division '/' (not '//') in: {}".format(directory))
    print("-" * 60)

    found_count = 0
    processed_files = 0

    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            # Process only files ending with .py (case-insensitive)
            if filename.lower().endswith(".py"):
                filepath = os.path.join(dirpath, filename)
                processed_files += 1
                try:
                    # Open with utf-8 encoding, ignore errors for robustness.
                    # Change encoding if needed (e.g., 'latin-1')
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        for line_num, line in enumerate(f, 1):
                            # Search for the pattern in the current line
                            if pattern.search(line):
                                # Optional: Check if the match is within a comment
                                # Find the index of the first '#'
                                comment_index = line.find('#')
                                # Search only in the part of the line before the comment
                                search_part = line if comment_index == -1 else line[:comment_index]

                                if pattern.search(search_part):
                                    # Optional: Could add checks to ignore matches inside strings,
                                    # but that significantly increases complexity.
                                    # This simpler check finds all potential locations.

                                    # Report the finding
                                    print("File: {}".format(filepath))
                                    print("Line {}: {}".format(line_num, line.rstrip()))
                                    print("-" * 20)
                                    found_count += 1

                except (IOError, OSError) as e:
                    # Handle potential file reading errors
                    print("Error reading file {}: {}".format(filepath, e))
                except Exception as e:
                    # Catch any other unexpected errors during file processing
                    print("Unexpected error processing file {}: {}".format(filepath, e))


    print("-" * 60)
    print("Search complete.")
    print("Processed {} Python files.".format(processed_files))
    print("Found {} potential instance(s).".format(found_count))


if __name__ == "__main__":
    # Check if a directory path is provided as a command-line argument
    if len(sys.argv) != 2:
        # Get the name of the script itself for the usage message
        script_name = os.path.basename(sys.argv[0])
        print("Usage: python {} <directory_to_search>".format(script_name))
        sys.exit(1) # Exit if incorrect number of arguments

    search_directory = sys.argv[1]
    find_potential_division(search_directory)