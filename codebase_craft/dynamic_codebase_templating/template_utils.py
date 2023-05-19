from rich.tree import Tree


# Assuming `outline` is a dictionary where each key is a directory and each value is a list of files
def print_outline_to_console(outline, console):
    tree = Tree("Project")
    for directory, files in outline.items():
        dir_branch = tree.add(directory)
        for file in files:
            dir_branch.add(file)

    console.print(tree)
