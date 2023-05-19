# codebase.py

import typer
from codebase_craft.dynamic_codebase_templating import (
    codebase_scanning,
    template_manager,
)
from codebase_craft.dynamic_codebase_templating.template_utils import (
    print_outline_to_console,
)
from codebase_craft.utils import openai_api
from rich.console import Console
from rich.logging import RichHandler
import logging
from codebase_craft.codebase_setup import (
    dependency_management,
    deployment_scripts,
    environment_setup,
    infra_as_code,
    setup_utils,
)
from codebase_craft.utils.config import load_config

from codebase_craft.codebase_setup.directory_setup import (
    create_directory,
    setup_directory,
)

# Setup the Rich console
console = Console()

# Setup the Rich logger
logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(console=console)],
)

logger = logging.getLogger("rich")

app = typer.Typer(name="codebase")


@app.command()
def scan():
    """
    Scan a directory and generate an outline of the codebase.
    """
    logger.info("Scanning directory...")
    outline = codebase_scanning.scan_directory()
    logger.info("Directory scanned. Generating template...")
    template = openai_api.run_template_generation(outline)
    logger.info("Template generated. Storing template...")
    template_manager.store_template(template)
    console.print("Finished scanning directory and storing template.", style="green")


@app.command()
def setup(
    template: str,
    name: str = typer.Option(..., prompt="Please enter a project name"),
):
    """
    Setup a new project from a template.
    """

    template_manager.reformat_template(logger, template)
    logger.info(f"Loading template: {template}")
    template = template_manager.load_template(logger, template)

    logger.info(f"Creating the project codebase directory for {name}")
    create_directory(name, logger)

    logger.info(f"Setting up the {name}/ directory")
    setup_directory(template, name, logger)

    logger.info("Setup complete.")


def main():
    app()


if __name__ == "__main__":
    main()
