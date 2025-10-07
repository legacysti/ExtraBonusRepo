from fasthtml.common import *

def task_list(tasks):
    items = []
    for task in tasks:
        style = "text-decoration:line-through;" if task['completed'] else ""
        items.append(Li(task['text'], style=style))
    return Ul(*items)

