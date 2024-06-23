from sqladmin import Admin, ModelView

from src.main import app
from src.database import engine

admin = Admin(app, engine)

# register model below
