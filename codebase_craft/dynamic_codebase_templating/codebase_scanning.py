import os
from codebase_craft.utils.handlers import (
    log_info,
    log_error,
    print_success,
    print_info,
    start_progress_task,
    update_progress,
)


class CodebaseScanner:
    def __init__(self):
        self.outline = {}
        self.languages = set()

    def scan(self, root="."):
        exclude_dirs = {
            ".venv",
            "node_modules",
            ".vscode",
            "*.egg-info",
            ".git",
            "*.cache",
        }

        log_info("Scanning directory...")

        total_files = sum([len(files) for r, d, files in os.walk(root)])
        progress_task = start_progress_task(total_files, "Scanning files")

        for root, dirs, files in os.walk(root):
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            for file in files:
                self.outline[file] = os.path.join(root, file)
                update_progress(progress_task)

                if file.endswith(".py"):
                    self.languages.add("Python")
                elif file.endswith(".js"):
                    self.languages.add("JavaScript")

        self.outline["languages"] = list(self.languages)

        print_success("Scanning completed!")
        return self.outline

    def get_languages(self):
        return list(self.languages)

    def get_directory_outline(self):
        return self.outline

    def print_to_console(self):
        print_info("Directory Outline:")
        for file, path in self.outline.items():
            print_info(f"{file}: {path}")

        print_info("\nLanguages Detected:")
        for language in self.languages:
            print_info(language)

    def gather_metadata(self):
        metadata = {
            "num_files": len(self.outline),
            "num_python_files": len(
                [file for file in self.outline if file.endswith(".py")]
            ),
            "num_js_files": len(
                [file for file in self.outline if file.endswith(".js")]
            ),
            "languages": list(self.languages),
        }
        return metadata
