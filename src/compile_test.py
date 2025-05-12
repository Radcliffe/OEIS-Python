"""
Find each python script in the seqs directory (recursively) and see if it can be imported
without error. Create a file with the name of the script and the error message if it cannot be imported.
"""

import os
from pathlib import Path
from typing import List, Tuple
import py_compile
from collections import Counter

bad_prints = []


def compile_all_scripts(python_dir: Path) -> List[Tuple[str, str]]:
    """
    Find Python scripts in the OEIS sequence directory.

    Args:
        python_dir (Path): Path to the Python scripts directory.

    Returns:
        List[Tuple[str, str]]: List of tuples containing the file path and script content.
    """
    compile_errors = []
    for root, _, files in sorted(os.walk(python_dir)):
        for file in files:
            if file.endswith(".py"):
                file_path = Path(root) / file
                try:
                    # Compile the script to check for syntax errors
                    py_compile.compile(file_path, cfile=file_path.with_suffix(".pyc"), doraise=True)
                except py_compile.PyCompileError as e:
                    # If there is a syntax error, add it to the list
                    stem = file_path.stem
                    if '_' in stem:
                        sequence_number, index = stem.split("_")
                        index = int(index)
                    else:
                        sequence_number = stem
                        index = 1
                    line_no = int(e.msg.split()[3]) - 4
                    short_error = e.msg.split('\n')[-2]
                    error_type = detect_error(short_error)
                    compile_errors.append((sequence_number, index, line_no, error_type, short_error))

    return compile_errors


# def fix_print_statement(file_path: Path, line_number: int):
#     """
#     Fix the print statement in the script.
#
#     Args:
#         file_path (Path): Path to the script.
#         line_number (str): Line number where the error occurred.
#     """
#     with open(file_path, 'r', encoding='utf-8') as file:
#         lines = file.readlines()
#
#     # Fix the print statement
#     lines[line_number - 1] = lines[line_number].replace("print ", "print(") + ")\n"
#
#     with open(file_path, 'w', encoding='utf-8') as file:
#         file.writelines(lines)
#     print(f"Fixed print statement in {file_path} at line {line_number}")


def write_report_excel(compile_errors: List[Tuple[str, str]], report_file: Path):
    """
    Write the compile errors to an Excel file.

    Args:
        compile_errors (List[Tuple[str, str]]): List of tuples containing the file path and error message.
        report_file (Path): Path to the report file.
    """
    import pandas as pd
    df = pd.DataFrame(compile_errors, columns=["Sequence", "Index", "Line", "Error type", "Error message"])
    df.to_excel(report_file, index=False)
    print(f"Report written to {report_file}. Found {len(compile_errors)} compile errors.")
    print(Counter(row[4] for row in compile_errors))

def write_report_markdown(compile_errors: List[Tuple[str, str]], report_file: Path):
    """
    Write the compile errors to a Markdown file.

    Args:
        compile_errors (List[Tuple[str, str]]): List of tuples containing the file path and error message.
        report_file (Path): Path to the report file.
    """
    with open(report_file, 'w') as f:
        f.write("# OEIS Python scripts that fail to compile in Python 3\n")
        f.write("| Sequence | Index | Line | Error type | Error message |\n")
        f.write("|----------|-------|------|------------|----------------|\n")
        for error in compile_errors:
            # Link sequence number to OEIS
            sequence_number = error[0]
            seq_link = f"[{sequence_number}](https://oeis.org/{sequence_number})"
            f.write(f"| {seq_link} | {error[1]} | {error[2]} | {error[3]} | {error[4]} |\n")
    print(f"Report written to {report_file}. Found {len(compile_errors)} compile errors.")



def remove_compiled_files(python_dir: Path):
    """
    Remove compiled Python files (.pyc) in the OEIS sequence directory.

    Args:
        python_dir (Path): Path to the OEIS sequence directory.
    """
    for root, _, files in os.walk(python_dir):
        for file in files:
            if file.endswith(".pyc"):
                file_path = Path(root) / file
                os.remove(file_path)


def detect_error(err_message: str) -> str:
    if "SyntaxError: Missing parentheses in call to 'print'." in err_message:
        return 'Print without parentheses'
    if "SyntaxError: invalid syntax" in err_message:
        return 'Invalid syntax'
    if "SyntaxError: 'return' outside function" in err_message:
        return 'Return outside function'
    return 'Unknown error'


if __name__ == "__main__":
    # Set the path to the OEIS sequence directory
    python_dir = Path("../pyscripts")
    # Find import errors
    compile_errors = compile_all_scripts(python_dir)
    # Write report to Excel file
    report_file = Path("compile_errors.xlsx")
    write_report_excel(compile_errors, report_file)
    # Write report to Markdown file
    report_file = Path("compile_errors.md")
    write_report_markdown(compile_errors, report_file)
    print(f"Found {len(compile_errors)} compile errors.")
    # Remove compiled files
    remove_compiled_files(python_dir)
    # print(*bad_prints, sep="\n")