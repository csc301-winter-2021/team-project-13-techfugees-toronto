import secrets
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from techfugees.main.config import Config


app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://fqgfknyjpfjowl:e49c966f9f6cd27166013693b017872b081cd278aeb843f32f19c34f6355d49d@ec2-34-225-103-117.compute-1.amazonaws.com:5432/dbd2rrpqdof8t'
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


