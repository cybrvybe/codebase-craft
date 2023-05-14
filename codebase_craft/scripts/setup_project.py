# setup_project.py

import os
import json
import yaml
import subprocess
import sys
import argparse
import logging
from typing import List

# Configure logging
logging.basicConfig(
    filename="project_setup.log",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s",
)


def install_dependencies(package_json_path: str) -> None:
    os.chdir(package_json_path)
    subprocess.run(["npm", "install"])


def main(
    project_name: str,
    project_directory_structure: str,
    package_json_template: str,
    additional_tools_and_libraries: List[str],
) -> None:
    # Load package.json template
    with open(package_json_template, "r") as f:
        try:
            package_json = json.load(f)
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding package.json file: {e}")
            return

    # Create the project directory
    os.makedirs(project_name, exist_ok=True)
    logging.info(f"Created the project directory: {project_name}")

    # Save the package.json content to a file
    with open(f"./{project_name}/package.json", "w") as f:
        json.dump(package_json, f, indent=4)

    # Create the directories based on the yaml template
    with open(project_directory_structure, "r") as f:
        try:
            directories = yaml.safe_load(f)
        except yaml.YAMLError as e:
            logging.error(f"Error decoding YAML file: {e}")
            return

    for directory in directories:
        os.makedirs(os.path.join(project_name, directory), exist_ok=True)

    logging.info(
        f"Created directories based on the YAML template: {project_directory_structure}"
    )

    # Install dependencies
    install_dependencies(f"./{project_name}")
    logging.info(f"Installed dependencies from package.json: {package_json_template}")

    # Install additional tools and libraries
    for tool in additional_tools_and_libraries:
        subprocess.run(["npm", "install", tool])

    logging.info(
        f"Installed additional tools and libraries: {additional_tools_and_libraries}"
    )

    # Initialize git and setup the remote repository
    os.chdir(project_name)
    subprocess.run(["git", "init"])

    # Add all files and make an initial commit
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Initial commit"])

    logging.info("Initialized git and made initial commit")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Set up a new project.")
    parser.add_argument("project_name", type=str, help="The name of the new project.")
    parser.add_argument(
        "project_directory_structure",
        type=str,
        help="The YAML file containing the project directory structure template.",
    )
    parser.add_argument(
        "package_json_template",
        type=str,
        help="The JSON file containing the package.json template.",
    )
    parser.add_argument(
        "additional_tools_and_libraries",
        nargs="*",
        help="Additional tools and libraries to install.",
    )
    args = parser.parse_args()
    main(
        args.project_name,
        args.project_directory_structure,
        args.package_json_template,
        args.additional_tools_and_libraries,
    )
