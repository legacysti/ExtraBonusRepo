from fasthtml.common import *

def task_list(tasks):
    items = []
    for task in tasks:
        style = "text-decoration:line-through;" if task['completed'] else ""
        items.append(
            Li(
                Input(
                    type="checkbox",
                    checked=task['completed'],
                    hx_post=f"/completed/{task['id']}",
                    hx_target="#task-list",
                    hx_swap="outerHTML"
                ),
                Span(task['text'], style=style),
                Button(
                    "×",
                    hx_post=f"/delete/{task['id']}",
                    hx_target="#task-list",
                    hx_swap="outerHTML",
                    style="margin-left:auto;border:none;background:none;color:red;font-size:1.5rem;cursor:pointer;"
                ),
                style="display:flex;align-items:center;gap:.5rem;margin-bottom:.5rem;"
            )
        )
    return Ul(*items, id="task-list", style="list-style:none;padding:0;")

