import venv
import os
import typer
import subprocess

app = typer.Typer()


class DependencyManager:
    def __init__(self, logger):
        self.logger = logger

    def install_dependencies(self):
        return None

    def install_python_dependencies(self):
        return None

    def install_node_dependencies(self):
        return None

    def setup_environments(self):
        """
        Setup Python virtual environment and/or Node.js environment based on the codebase languages.
        """
        for root, languages in global_state.items():
            if "Python" in languages:
                self.setup_python_environment(root)
            if "JavaScript" in languages:
                self.setup_node_environment(root)

    def setup_python_environment(directory):
        """
        Setup a Python virtual environment in the given directory.
        """
        venv_dir = os.path.join(directory, ".venv")
        venv.create(venv_dir, with_pip=True)

        # Install Python dependencies
        requirements_file = os.path.join(directory, "requirements.txt")
        if os.path.exists(requirements_file):
            subprocess.run(
                [
                    os.path.join(venv_dir, "bin", "pip"),
                    "install",
                    "-r",
                    requirements_file,
                ]
            )

    def setup_node_environment(directory):
        """
        Setup a Node.js environment in the given directory.
        """
        # Install Node.js dependencies
        package_json_file = os.path.join(directory, "package.json")
        if os.path.exists(package_json_file):
            subprocess.run(["npm", "install"], cwd=directory)


@app.command()
def setup_directory(template_data, project_name, logger):
    manager = DependencyManager(logger)


if __name__ == "__main__":
    app()
