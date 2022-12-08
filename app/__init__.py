from config import Config
from flask import Flask, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


db = SQLAlchemy()
migrate = Migrate()
login_manager= LoginManager()

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)
login_manager.init_app(app)


from app.blueprints.main import bp as main_bp
app.register_blueprint(main_bp)
from app.blueprints.blog import bp as blog_bp
app.register_blueprint(blog_bp)
from app.blueprints.auth import bp as auth_bp
app.register_blueprint(auth_bp)
from app.blueprints.api import bp as api_bp
app.register_blueprint(api_bp)

login_manager.login_view = 'auth.sign_in'
login_manager.login_message = 'You cannot see this!'
login_manager.login_message_category = 'danger'
