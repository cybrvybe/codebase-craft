# codebase.py

import typer
from rich.console import Console
from rich.logging import RichHandler
import logging
from codebase_craft.utils.config import load_config
from codebase_craft.commands import directory_commands, setup_commands


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
    directory_commands.scan_command(logger, console)


@app.command()
def tree():
    """
    Print the dir tree to the console
    """
    directory_commands.print_tree_command(logger, console)


@app.command()
def setup(
    template: str,
    name: str = typer.Option(..., prompt="Please enter a project name"),
):
    """
    Setup a new project from a template.
    """
    setup_commands.setup_command(logger, console, name, template)


def main():
    app()


if __name__ == "__main__":
    main()
