# my_tasks_app.py

from fasthtml.common import *

from components.add_task_v5 import add_task_section
from components.task_list_v4 import task_list

app, rt = fast_app()

# Global CSS: set border width to 1px for header & sections
BORDERS = Style("""
header, section {
    border: 1px solid #000; # had to manually add this to see the borders
    padding: 1rem;
    margin-bottom: 1rem;
}
""")



tasks = [
    {'id': 1, 'text': 'Buy groceries', 'completed': False},
    {'id': 2, 'text': 'Email project report', 'completed': True},
    {'id': 3, 'text': 'Workout 30 minutes', 'completed': False},
]


@rt("/")
def home():
    return Titled(
        "",
        BORDERS,
        Header(H1("MY TASKS")),
        Section(add_task_section()),
        Section(task_list(tasks))
    )


@rt("/add")
def post(text: str):
    # added this for debugging
    print(f"In the /add route. Received text: {text}")     
    if text.strip():
        new_id = max([task['id'] for task in tasks]) + 1 if tasks else 1
        tasks.append({'id': new_id, 'text': text.strip(), 'completed': False})

    return task_list(tasks)

@rt("/completed/{task_id}")
def post(task_id: int):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = not task['completed']
            break
    return task_list(tasks)

@rt('/test')
def test():
    return "Test works!"

@rt("/delete/{task_id}")
def post(task_id: int):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return task_list(tasks)



if __name__ == "__main__":
    serve()


