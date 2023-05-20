from codebase_craft.dynamic_codebase_templating import (
    codebase_scanning,
    template_manager,
)
from codebase_craft.utils import openai_api, print_tree
import os


def scan_command(logger, console):
    logger.info("Scanning directory...")
    outline = codebase_scanning.scan_directory()
    logger.info("Directory scanned. Generating template...")
    template = openai_api.run_template_generation(outline)
    logger.info("Template generated. Storing template...")
    template_manager.store_template(template)
    console.print("Finished scanning directory and storing template.", style="green")


def print_tree_command(logger, console):
    console.print("Creating tree ...", style="blue")
    path = os.getcwd()
    tree = print_tree.create_tree(path)
    print_tree.print_tree(tree)
    console.print("Finished printing the directory", style="green")
