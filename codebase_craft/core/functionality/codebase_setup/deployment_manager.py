import typer

app = typer.Typer()


class DeploymentManager:
    def __init__(self, logger):
        self.logger = logger
