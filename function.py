FILEPATH = "todo.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos

def write_todos(todo, filepath=FILEPATH):
    with open(filepath, "a") as file:
        file.writelines(todo)

def delete_todo(todo, filepath=FILEPATH):
    todos = get_todos()
    todos.remove(todo)
    with open(filepath, "w") as file:
        file.writelines(todos)
    
    