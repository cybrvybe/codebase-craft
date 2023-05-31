# entry.py
import typer
import logging
from codebase_craft.utils.config import load_config
from codebase_craft.commands import directory_commands, setup_commands
from codebase_craft.utils.handlers import pretty_print
from codebase_craft.utils.console import console


logger = logging.getLogger("rich")

app = typer.Typer(name="codebase")


@app.command()
def scan():
    """
    Scan a directory and generate an outline of the codebase.
    """
    directory_commands.scan_command()


@app.command()
def tree():
    """
    Print the dir tree to the console
    """
    directory_commands.print_tree_command()


@app.command()
def setup(
    template: str,
    name: str = typer.Option(..., prompt="Please enter a project name"),
):
    """
    Setup a new project from a template.
    """
    pretty_print(f"Setting up project: {name} using template: {template}")
    setup_commands.setup_command(logger, console, name, template)


def main():
    app()


if __name__ == "__main__":
    main()
