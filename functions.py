FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(param_todos, filepath=FILEPATH):
    """ Write the list of to-do items in a text file """
    with open(filepath, 'w') as file_local:
        file_local.writelines(param_todos)


if __name__ == "__main__":
    print("hello from functions")