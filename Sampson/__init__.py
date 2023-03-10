from flask import Flask
from Sampson.config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


admin = Admin(template_mode='bootstrap3')
db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)
    admin.init_app(app)
    Bootstrap(app)
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)

    from Sampson.models import Tbproductsme
    admin.add_view(ModelView(Tbproductsme,db.session))

    from Sampson.mainpage.views import mainbp
    app.register_blueprint(mainbp)


    return app