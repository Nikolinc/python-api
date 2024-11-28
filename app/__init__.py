from flask import Flask
from .db import get_db_connection
from .models import create_table

def create_app():
    app = Flask(__name__)
    conn = get_db_connection()
    create_table(conn)
    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app
