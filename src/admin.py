from sqladmin import ModelView

from src.app.model import User


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.name]


# create admin view
