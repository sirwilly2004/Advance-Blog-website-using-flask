from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flaskblog.config import Config


# database configuration

db = SQLAlchemy()

# bcrypt configuration
bcrypt = Bcrypt()
# flask_login configuration
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
# flask_mail configuration
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
mail = Mail()
# 465
# xcxf jwbv rsjc ypya (password for gmail 2 app password)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.admin.routes import admin
    from flaskblog.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(main)
    app.register_blueprint(posts)
    app.register_blueprint(admin)
    app.register_blueprint(errors)

    return app