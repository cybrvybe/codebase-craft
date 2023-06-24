import typer

app = typer.Typer()


class DbSetup:
    def __init__(self, logger):
        self.logger = logger

    def create_db(self):
        return None

    def set_up_tables(self):
        return None

    def init_db_seed(self):
        return None
