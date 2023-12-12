from flask import Flask

from app.config import Config

from app.models.base import db

from app.routes.agents import agents_bp
from app.routes.customers import customers_bp
from app.routes.calls import calls_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(agents_bp)
    app.register_blueprint(customers_bp)
    app.register_blueprint(calls_bp)

    return app
