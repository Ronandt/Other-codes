#__init__.py makes a python package (will run autoamtically once import parent folder (website))
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__) # Tells the name of the file to let Flask know which file to look for
    app.config["SECRET_KEY"] = "shiraori" #Secure cookies or encrypt session data reltaed to website and the secret key https://flask.palletsprojects.com/en/2.0.x/config/
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}" #https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/. My SQL database is stored in {DB_NAME}

    db.init_app(app) #Take this database youo've defned and this is the app you're gonna use with this database (FLASK) https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/
 
    from .views import views #importing the variables from the file with a .
    from .auth import auth
    app.register_blueprint(views, url_prefix="/") #e.g if url_prefix was "hello" and views.py route is views.route("yes") we would go to /hello/yes in the website
    app.register_blueprint(auth, url_prefix="/") #slash means no prefix
    #regsitering blueprint
    from .models import User #relative import
    create_database(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' #in auth page go to login
    login_manager.init_app(app)
    @login_manager.user_loader #what user you're looking for and use this function to load the user
    def load_user(id):
        return User.query.get(int(id)) #telling flask how we load user (looks for primary key)
    return app
def create_database(app):
    if not path.exists('website/' + DB_NAME): #check if db exists
        db.create_all(app=app) #creates database (Tell which app it is used for and creates database at the sqlalchemy_database_URI)
        print("Created Database!")