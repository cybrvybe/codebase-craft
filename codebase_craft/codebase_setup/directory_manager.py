import os
import typer
from codebase_craft.utils.config import load_config

app = typer.Typer()


class DirectoryManager:
    def __init__(self, logger):
        self.logger = logger

    def create_directory(self, path):
        try:
            os.makedirs(path)
        except OSError as e:
            self.logger.info(f"Error: {e}")
        else:
            self.logger.info(f"Successfully created the directory {path}")

    def create_file(self, path):
        try:
            with open(path, "w") as f:
                f.write("Placeholder content")
        except OSError as e:
            self.logger.info(f"Error: {e}")
        else:
            self.logger.info(f"Successfully created the file {path}")

    def create_structure(self, structure, path):
        for key, value in structure.items():
            new_path = os.path.join(path, key)
            if isinstance(value, dict):  # It's a directory
                os.makedirs(new_path, exist_ok=True)
                self.create_structure(value, new_path)
            else:  # It's a file
                self.create_file(new_path)


@app.command()
def setup_directory(template_data, project_name, logger):
    config = load_config()

    """
    Set up the directory structure from the JSON file.
    """
    logger.info(
        f"Setting up directory structure for C:/Users/alexf/software-projects")

    creator = DirectoryManager(logger)

    main_dir_path = os.path.join(
        "C:/Users/alexf/software-projects", project_name)
    os.makedirs(main_dir_path, exist_ok=True)
    creator.create_structure(template_data, main_dir_path)

    logger.info("Directory setup complete.")


if __name__ == "__main__":
    app()
