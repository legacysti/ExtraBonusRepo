from fasthtml.common import *

from fasthtml.common import *

def add_task_section(input_name: str = "text"):
    return Form(
        Input(type="text", id="new-task", name=input_name, placeholder="Enter a new task...", required=True),
        Button("Add", type="submit", onclick="event.preventDefault(); alert('Add: ' + document.getElementById('new-task').value);"),
        method="post",
        action="/add",
        style="display:flex;gap:.5rem;align-items:center;"
    )
