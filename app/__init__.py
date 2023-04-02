from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_pyfile('config.py')




db = SQLAlchemy(app)




login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = u"Bonvolu ensaluti por uzi tiun paĝon."



from app import models, forms, views