import secrets
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from techfugees.main.config import Config


app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app) #ORM
bcrypt = Bcrypt(app) #hashing
login_manager = LoginManager(app) #session management
login_manager.login_view = 'users.login' #default view for login
login_manager.login_message_category = 'info' #setting bootstrap class for login validaiton message


from techfugees.users.routes import users #blueprint instance
from techfugees.posts.routes import posts
from techfugees.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)


