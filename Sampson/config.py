import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    SECRET_KEY = "my_secret_key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "data.sqlite")
    FLASK_ADMIN_SWATCH = 'sandstone'

