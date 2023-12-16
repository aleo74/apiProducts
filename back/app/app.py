from flask import Flask
from app.config import config
from app.routes.api import main_bp
from dotenv import load_dotenv

load_dotenv()


def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config[config_name].PSQL_URI
    app.register_blueprint(main_bp)

    return app


def prepare_db(app):
    with app.app_context():
        from app.db import db
        db.init_app(app)
        db.create_all()
        db.session.commit()
