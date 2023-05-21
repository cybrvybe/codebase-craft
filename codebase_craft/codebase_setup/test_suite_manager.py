import typer

app = typer.Typer()


class TestSuiteManager:
    def __init__(self, logger):
        self.logger = logger

    def setup_test_suite(self):
        return None

    def run_test_suite(self):
        return None
