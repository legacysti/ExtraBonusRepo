from fasthtml.common import *

def add_task_section(input_name: str = "text"):
    return Form(
        Input(type="text", id="new-task", name=input_name, placeholder="Enter a new task...", required=True),
        Button("Add", type="submit"),
        method="post",
        action="/add",
        hx_post="/add",
        hx_target="#task-list",
        hx_swap="outerHTML",
        hx_on__after_request="document.getElementById('new-task').value=''",
        style="display:flex;gap:.5rem;align-items:center;"
    )

