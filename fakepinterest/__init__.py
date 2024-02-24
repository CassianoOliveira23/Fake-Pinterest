from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://projetoflask_db_user:GVB45fgLcPycsvYYmZpR72KZDESyLMB3@dpg-cnd37l7109ks738qqcv0-a/projetoflask_db"
app.config["SECRET_KEY"] = "9944a393393d275f3a9e27be64a64ca3"
app.config["UPLOAD_FOLDER"] = "static/fotos_post"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"

from fakepinterest import routes