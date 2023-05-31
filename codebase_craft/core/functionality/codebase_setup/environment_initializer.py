import typer

app = typer.Typer()


class EnvironmentInitializer:
    def __init__(self, logger):
        self.logger = logger

    def check_system_level_dependencies(self):
        return None

    def check_correct_language_runtime(self):
        return None

    def setup_venv(self):
        return None
