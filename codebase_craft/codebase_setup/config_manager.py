import typer

app = typer.Typer()


class ConfigManager:
    def __init__(self, logger):
        self.logger = logger

    def setup_env_files(self):
        return None

    def setup_linters_and_formatters(self):
        return None

    def setup_setup_files(self):
        return None

    def setup_setup_dot_py(self):
        return None

    def setup_package_json(self):
        return None
