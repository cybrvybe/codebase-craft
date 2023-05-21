import typer

app = typer.Typer()


class VersionControlManager:
    def __init__(self, logger):
        self.logger = logger

    def init_local_git_repo(self):
        return None

    def add_init_files_to_staging(self):
        return None

    def init_commit(self):
        return None

    def commit(self):
        return None
