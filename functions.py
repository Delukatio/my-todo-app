FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH):
    """Retrieves the todos from file"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Saves the todos variable to file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

