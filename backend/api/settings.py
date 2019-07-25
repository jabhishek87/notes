import os

DB_NAME = os.getenv("DB_NAME", "app.db")

# project_base_dir
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, DB_NAME)
