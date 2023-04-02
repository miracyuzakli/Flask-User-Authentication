import os
import secrets


CURRENT_DIR = os.getcwd()




SQLALCHEMY_DATABASE_URI = 'sqlite:///' + CURRENT_DIR + '/database.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False


SECRET_KEY = secrets.token_hex()