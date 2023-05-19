import os
import yaml
import re
import logging
import argparse


# Set up a logger for this script
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def is_excluded(path):
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
    if "\\.git\\" in path:
        return True

    return False


def print_and_save_tree(args=None):
    logger.info("Running print_and_save_tree()")
    path = os.getcwd()
    logger.info(f"Current working directory: {path}")
    tree = create_tree(path)

    if args and args.yaml:
        logger.info("In if args and args.yaml:")
        save_tree_to_yaml(tree)
    else:
        print_tree(tree)


def save_tree_to_yaml(tree):
    logger.info("Attempting to save yaml file...")
    try:
        # Specify the full path of the output file
        output_path = os.path.join(
            os.getcwd(), "codebase_craft", "templates", "snapshots", "tree.yaml"
        )
        with open(output_path, "w") as file:
            yaml.dump(tree, file)
        logger.info("Yaml file saved successfully.")
    except Exception as e:
        logger.error("Failed to save yaml file.", exc_info=True)


def print_tree(tree, indent=""):
    for key, value in tree.items():
        print(f"{indent}{key}")
        if isinstance(value, dict):
            print_tree(value, indent + "  ")


def create_tree(path, tree=None):
    if tree is None:
        tree = {}

    for item in os.scandir(path):
        if item.is_file() and not is_excluded(item.path):
            tree[item.name] = None
        elif item.is_dir() and not is_excluded(item.path):
            tree[item.name] = create_tree(item.path, {})

    return tree


def main():
    parser = argparse.ArgumentParser(
        description="Print and possibly save the project tree."
    )
    parser.add_argument("--yaml", help="Save tree to a yaml file", action="store_true")
    args = parser.parse_args()
    print_and_save_tree(args)


if __name__ == "__main__":
    main()
