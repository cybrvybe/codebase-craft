import argparse
import os
import subprocess
import logging
from . import config


class Project:
    def __init__(self, name):
        self.name = name

    def create_directories(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('name')
        args = parser.parse_args([self.name])
        script_path = os.path.join(config.SCRIPT_DIR, 'create_directories.sh')
        subprocess.run(['bash', script_path, args.name])

    def print_and_save_tree(self):
        script_path = os.path.join(config.SCRIPT_DIR, 'print_tree.py')
        subprocess.run(['python', script_path])

    def setup_project(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('name')
        args = parser.parse_args([self.name])
        script_path = os.path.join(config.SCRIPT_DIR, 'setup_project.py')
        subprocess.run(['python', script_path, args.name])

    def _run_bash_script(self, script_path, arg):
        subprocess.run(['bash', script_path, arg])

    def _run_python_script(self, script_path, *args):
        # Convert arguments from Namespace to list
        args_list = [str(getattr(args, arg)) for arg in vars(args)]

        # Run the script with arguments
        subprocess.run(['python', script_path, *args_list])
