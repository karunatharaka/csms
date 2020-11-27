from flask import Flask
from config import Config
#from flask_sqlalchemy import SQLAlchemy
#from flask_bcrypt import Bcrypt
#from flask_login import LoginManager
#from flask_migrate import Migrate


app = Flask(__name__)

app.config.from_object(Config)

from app import routes

#app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#db = SQLAlchemy(app)

#migrate = Migrate(app, db)

#bcrypt = Bcrypt(app)

#login_manager = LoginManager(app)

