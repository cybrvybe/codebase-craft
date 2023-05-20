from codebase_craft.dynamic_codebase_templating import (
    codebase_scanning,
    template_manager,
)
from codebase_craft.utils import openai_api, print_tree
import os


from codebase_craft.utils.handlers import (
    log_info,
    print_success,
    print_info,
    start_progress_task,
    update_progress,
)


def scan_command():
    log_info("Scanning directory...")
    task_id = start_progress_task(100, "Scanning directory")

    outline = codebase_scanning.scan_directory()
    update_progress(task_id, 50)

    log_info("Directory scanned. Generating template...")
    template = openai_api.run_template_generation(outline)
    update_progress(task_id, 75)

    log_info("Template generated. Storing template...")
    template_manager.store_template(template)
    update_progress(task_id, 100)

    print_success("Finished scanning directory and storing template.")


def print_tree_command():
    print_info("Creating tree ...")
    path = os.getcwd()
    tree = print_tree.create_tree(path)
    print_tree.print_tree(tree)
    print_success("Finished printing the directory")
