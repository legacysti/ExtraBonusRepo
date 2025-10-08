from fasthtml.common import *
from pages.add_user import add_user_page
from pages.list_users import list_users_page

app, rt = fast_app()

list_of_users = [
{"id":"1", "first_name":"John", "last_name":"Doe"},
{"id":"2","first_name":"Jane", "last_name":"Doe"}
]

@rt('/')
def get():
    return add_user_page()

@rt('/list_users')
def get():
    return list_users_page(list_of_users)

@rt('/delete')
def post(user_id: str):
    global list_of_users
    list_of_users = [user for user in list_of_users if user["id"] != user_id]
    return RedirectResponse('/list_users', status_code=303)

@rt('/add_user')
def post(first_name: str, last_name: str):
    global list_of_users
    new_id = str(max([int(user["id"]) for user in list_of_users]) + 1) if list_of_users else "1"
    
    list_of_users.append({
        "id": new_id,
        "first_name": first_name,
        "last_name": last_name
    })
    
    return 
serve()