# dynamic_codebase_templating/codebase_scanning.py

import os


def scan_directory():
    """
    Scan a directory and generate an outline of the codebase.
    If no directory is specified, scan the current directory.
    """
    outline = {}
    exclude_dirs = {".venv", "node_modules", ".vscode", "*.egg-info", ".git"}

    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in files:
            # Add file to outline
            outline[file] = os.path.join(root, file)
    return outline
