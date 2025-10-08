from fasthtml.common import *

def user_row_entry(user):
    return Tr(
        Td(user["first_name"]),
        Td(user["last_name"]),
        Td(
            Form(
                Input(type="hidden", name="user_id", value=user["id"]),
                Button("X", type="submit"),
                method="post",
                action="/delete"
            )
        )
    )