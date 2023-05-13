import os
import re


def is_excluded(path, git_ignore_patterns=[]):
    file_name = os.path.basename(path)

    # Exclude names that are just long strings of incoherent text or numbers
    if re.match(r"^[a-z0-9]{15,}$", file_name) or re.match(
        r"^[a-fA-F0-9]{64}\.json\.gz$", file_name
    ):
        return True

    if "\\node_modules\\" in path:
        return True
    if "\\.cache\\" in path:
        return True

    if "\\.venv\\" in path:
        return True

    # Exclude files/directories matching .gitignore patterns
    for pattern in git_ignore_patterns:
        # Convert wildcard character to regex equivalent
        regex_pattern = re.escape(pattern).replace("\\*", ".*")
        if re.match(regex_pattern, file_name):
            return True

    return False


def process_file(path, indent=""):
    if not is_excluded(path):
        # It's a valid file, so print its name
        print(f"{indent}{os.path.basename(path)}")


def process_directory(path, indent=""):
    if not is_excluded(path):
        # It's a valid directory, so print its name
        print(f"{indent}{os.path.basename(path)}/")

        # Then recursively print its children
        next_indent = f"  {indent}"
        for item in os.scandir(path):
            if item.is_file():
                process_file(item.path, next_indent)
            elif item.is_dir():
                process_directory(item.path, next_indent)


def print_tree(path=os.getcwd(), indent=""):
    if os.path.isdir(path):
        process_directory(path, indent)
    else:
        process_file(path, indent)


# Call the function for the current directory
print_tree()
