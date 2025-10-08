from fasthtml.common import *
from components.user_row_entry import user_row_entry

def list_user_table(list_of_users):
    rows = [user_row_entry(user) for user in list_of_users]
    
    return Titled("List Users", 
        Table(
            Tr(Th("First Name"), Th("Last Name"), Th("Actions")),
            *rows
        )
    )