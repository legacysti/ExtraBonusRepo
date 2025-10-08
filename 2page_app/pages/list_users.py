from fasthtml import components
from fasthtml.common import *
from components.list_user_table import list_user_table


def list_users_page(list_of_users):
    return list_user_table(list_of_users)
    