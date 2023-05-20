from codebase_craft.dynamic_codebase_templating import template_manager
from codebase_craft.codebase_setup.directory_setup import (
    create_directory,
    setup_directory,
)


def setup_command(logger, console, project_name, template):
    template_manager.reformat_template(logger, template)
    logger.info(f"Loading template: {template}")
    template = template_manager.load_template(logger, template)

    logger.info(f"Creating the project codebase directory for {project_name}")
    create_directory(project_name, logger)

    logger.info(f"Setting up the {project_name}/ directory")
    setup_directory(template, project_name, logger)

    console.print("Setup complete.", style="green")
