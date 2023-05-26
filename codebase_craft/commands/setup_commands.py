from codebase_craft.dynamic_codebase_templating import template_manager
from codebase_craft.codebase_setup.directory_manager import (
    DirectoryManager
)

from codebase_craft.utils.handlers import (
    log_info,
    print_success,
    start_progress_task,
    update_progress,
)


def setup_command(logger, console, project_name, template):
    log_info(f"Loading template: {template}")
    template = template_manager.load_template(logger, template)
    dir_manager = DirectoryManager(logger)

    task_id = start_progress_task(
        100, f"Setting up the {project_name} directory")
    log_info(f"Creating the project codebase directory for {project_name}")
    dir_manager.create_directory(project_name, logger)
    update_progress(task_id, 50)

    log_info(f"Setting up the {project_name}/ directory")
    dir_manager.setup_directory(template, project_name, logger)
    update_progress(task_id, 50)

    print_success("Setup complete.")
