from fasthtml.common import *
from components.add_user import add_user

def add_user_page():
    return Titled(
        Form(
            Div(
                Label("First Name"),
                Input(type="text", name="first_name")
            ),
            Div(
                Label("Last Name"),
                Input(type="text", name="last_name")
            ),
            Button("Confirm", type="submit"),
            method="post",
            action="/add_user"
        )
    )