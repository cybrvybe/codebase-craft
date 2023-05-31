import typer

app = typer.Typer()


class CiCdPipelineManager:
    def __init__(self, logger):
        self.logger = logger

    def setup_pipeline(self):
        return None
