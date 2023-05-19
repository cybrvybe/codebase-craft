import os
import typer
from codebase_craft.utils.config import load_config

app = typer.Typer()


def create_directory(path, logger):
    try:
        os.makedirs(path)
    except OSError as e:
        logger.info(f"Error: {e}")
    else:
        logger.info(f"Successfully created the directory {path}")


def create_file(path, logger):
    try:
        with open(path, "w") as f:
            f.write("Placeholder content")
    except OSError as e:
        logger.info(f"Error: {e}")
    else:
        logger.info(f"Successfully created the file {path}")


@app.command()
def setup_directory(template_data, project_name, logger):
    config = load_config()

    """
    Set up the directory structure from the JSON file.
    """
    logger.info(f"Setting up directory structure for C:/Users/alexf/software-projects")

    def create_structure(structure, path):
        for key, value in structure.items():
            new_path = os.path.join(path, key)
            if isinstance(value, dict):  # It's a directory
                os.makedirs(new_path, exist_ok=True)
                create_structure(value, new_path)
            else:  # It's a file
                create_file(new_path, logger)

    main_dir_path = os.path.join("C:/Users/alexf/software-projects", project_name)
    os.makedirs(main_dir_path, exist_ok=True)
    create_structure(template_data, main_dir_path)

    logger.info("Directory setup complete.")


if __name__ == "__main__":
    app()
