import argparse
from .project import Project
from .openai_api import generate_template

def default_function(args):
    print("No command provided. Please use 'create', 'tree', 'setup', or 'template'.")

def main():
    # Define the command-line interface
    parser = argparse.ArgumentParser(prog='codebase')
    subparsers = parser.add_subparsers()

    # Create the parser for the "create_directories" command
    parser_create = subparsers.add_parser('create', help='Create directories for a new project')
    parser_create.add_argument('name', help='The name of the new project')
    parser_create.set_defaults(func=Project.create_directories)

    # Create the parser for the "print_tree" command
    parser_print = subparsers.add_parser('tree', help='Print the tree structure of the current directory')
    parser_print.set_defaults(func=Project.print_and_save_tree)

    # Create the parser for the "setup_project" command
    parser_setup = subparsers.add_parser('setup', help='Set up a new project')
    parser_setup.set_defaults(func=Project.setup_project)

    # Create the parser for the "generate_template" command
    parser_template = subparsers.add_parser('template', help='Generate a generic template of the current directory structure')
    parser_template.set_defaults(func=generate_template)

    # Set the default function
    parser.set_defaults(func=default_function)

    # Parse the arguments and call the appropriate function
    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
