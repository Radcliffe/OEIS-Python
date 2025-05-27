#!/usr/bin/env python3
"""
Python Import Analyzer

Recursively scans a directory for Python files and analyzes import statements,
generating a Markdown report with import statistics.
"""

import os
import re
import argparse
from collections import defaultdict
from pathlib import Path


class ImportAnalyzer:
    def __init__(self):
        self.import_counts = defaultdict(int)
        self.file_imports = defaultdict(list)
        
        # Regex patterns for different import types
        self.import_patterns = [
            # Standard import: import module1, module2, module3
            r'^\s*import\s+([^\#\n]+)',
            # From import: from module import item1, item2
            r'^\s*from\s+([^\s\#]+)\s+import\s+([^\#\n]+)',
        ]
    
    def remove_comments_and_strings(self, line):
        """Remove comments and string literals from a line to avoid false positives."""
        # Remove string literals (both single and double quotes, including multiline)
        line = re.sub(r'""".*?"""', '', line, flags=re.DOTALL)
        line = re.sub(r"'''.*?'''", '', line, flags=re.DOTALL)
        line = re.sub(r'"[^"\\]*(?:\\.[^"\\]*)*"', '', line)
        line = re.sub(r"'[^'\\]*(?:\\.[^'\\]*)*'", '', line)
        
        # Remove comments (everything after #)
        comment_pos = line.find('#')
        if comment_pos != -1:
            line = line[:comment_pos]
        
        return line.strip()
    
    def extract_module_names(self, import_text):
        """Extract clean module names from import text."""
        modules = []
        # Split by comma and clean each module name
        for module in import_text.split(','):
            module = module.strip()
            # Remove 'as alias' part if present
            if ' as ' in module:
                module = module.split(' as ')[0].strip()
            if module:
                modules.append(module)
        return modules
    
    def analyze_file(self, file_path):
        """Analyze a single Python file for import statements."""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except Exception as e:
            print(f"Warning: Could not read {file_path}: {e}")
            return
        
        lines = content.split('\n')
        lines = [stmt for line in lines for stmt in line.split(';')]
        file_imports = set()
        
        for line_num, line in enumerate(lines, 1):
            # Remove comments and strings to avoid false positives
            clean_line = self.remove_comments_and_strings(line)
            
            if not clean_line:
                continue
            
            # Check for standard import statements
            match = re.match(self.import_patterns[0], clean_line)
            if match:
                import_text = match.group(1).strip()
                modules = self.extract_module_names(import_text)
                for module in modules:
                    # Get the top-level package name
                    top_level = module.split('.')[0]
                    self.import_counts[top_level] += 1
                    file_imports.add(top_level)
            
            # Check for from...import statements
            match = re.match(self.import_patterns[1], clean_line)
            if match:
                module = match.group(1).strip()
                # Get the top-level package name
                top_level = module.split('.')[0]
                self.import_counts[top_level] += 1
                file_imports.add(top_level)
        
        if file_imports:
            self.file_imports[str(file_path)] = sorted(file_imports)
    
    def scan_directory(self, directory):
        """Recursively scan directory for Python files."""
        directory = Path(directory)
        
        if not directory.exists():
            raise ValueError(f"Directory {directory} does not exist")
        
        if not directory.is_dir():
            raise ValueError(f"{directory} is not a directory")
        
        python_files = list(directory.rglob("*.py"))
        
        if not python_files:
            print("No Python files found in the directory")
            return
        
        print(f"Found {len(python_files)} Python files to analyze...")
        
        for file_path in python_files:
            self.analyze_file(file_path)
    
    def generate_report(self, output_file="../reports/import_report.md"):
        """Generate a Markdown report with import statistics."""
        if not self.import_counts:
            print("No imports found to report")
            return
        
        # Sort imports by count (descending)
        sorted_imports = sorted(self.import_counts.items(), key=lambda x: (-x[1], x[0]))
        
        # Generate report content
        report_lines = [
            "# Python Import Analysis Report",
            "",
            f"Total unique packages imported: {len(sorted_imports)}",
            f"Total import statements found: {sum(self.import_counts.values())}",
            f"Files analyzed: {len(self.file_imports)}",
            "",
            "## Import Statistics",
            "",
            "| Package | Import Count |",
            "|---------|--------------|"
        ]
        
        for package, count in sorted_imports:
            package = package.replace('_', r'\_')
            report_lines.append(f"| {package} | {count} |")

        # Write report to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(report_lines))
        
        print(f"Report generated: {output_file}")
        
        # Print summary to console
        print(f"\nSummary:")
        print(f"- {len(sorted_imports)} unique packages found")
        print(f"- {sum(self.import_counts.values())} total imports")
        print(f"- {len(self.file_imports)} files analyzed")
        print(f"\nTop 10 most imported packages:")
        for package, count in sorted_imports[:10]:
            print(f"  {package}: {count}")


def main():
    parser = argparse.ArgumentParser(description="Analyze Python imports in a directory")
    parser.add_argument("directory", help="Directory to analyze")
    parser.add_argument("-o", "--output", default="../reports/import_report.md", 
                       help="Output file for the report (default: import_report.md)")
    
    args = parser.parse_args()
    
    try:
        analyzer = ImportAnalyzer()
        analyzer.scan_directory(args.directory)
        analyzer.generate_report(args.output)
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
