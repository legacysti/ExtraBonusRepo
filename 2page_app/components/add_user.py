
from fasthtml.common import *

#@rt('/add_user')
def add_user(first_name: str, last_name: str):
    global list_of_users
    new_id = str(max([int(user["id"]) for user in list_of_users]) + 1) if list_of_users else "1"
    
    list_of_users.append({
        "id": new_id,
        "first_name": first_name,
        "last_name": last_name
    })
    
    return Div("confirm user submitted")