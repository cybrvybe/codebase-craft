import typer

app = typer.Typer()


class MetricsManager:
    def __init__(self, logger):
        self.logger = logger

    def store_metric(self, metric_name, metric_value):
        return None

    def get_programming_languages_used(self):
        return None

    def get_codebase_gpt_token_count(self):
        return None

    def get_libraries_used(self):
        return None

    def get_db_used(self):
        return None
