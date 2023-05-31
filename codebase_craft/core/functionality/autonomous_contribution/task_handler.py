import typer

app = typer.Typer()


class TaskHandler:
    def __init__(self, logger):
        self.logger = logger
