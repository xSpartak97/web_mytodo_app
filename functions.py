FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as f_local:
        todos_local = f_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write a to-do items list in the text file."""
    with open(filepath, 'w') as f_local:
        f_local.writelines(todos_arg)


