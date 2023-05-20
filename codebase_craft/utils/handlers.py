# utils/handlers.py

from codebase_craft.utils.console import console, logger, progress
from rich.prompt import Prompt
from rich.panel import Panel
from rich import print as rprint
from typing import Any


def log_info(message: str):
    logger.info(message)


def log_error(message: str):
    logger.error(message)


def log_warning(message: str):
    logger.warning(message)


def print_error(message: str):
    console.print(f"[bold red]{message}[/bold red]")


def print_success(message: str):
    console.print(f"[bold green]{message}[/bold green]")


def print_info(message: str):
    console.print(f"[bold blue]{message}[/bold blue]")


def start_progress_task(total: int, description: str = "") -> Any:
    return progress.add_task(description, total=total)


def update_progress(task_id: Any, advance: int = 1):
    progress.update(task_id, advance=advance)


def prompt_input(text: str) -> str:
    return Prompt.ask(text)


def confirm_action(text: str) -> bool:
    return Prompt.confirm(text)


def pretty_print(text: str):
    rprint(Panel(text))
