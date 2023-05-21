import typer

app = typer.Typer()


class BuildRunner:
    def __init__(self, logger):
        self.logger = logger

    def run_init_build(self):
        return None
