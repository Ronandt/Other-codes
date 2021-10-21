from website.views import home
==================================================================================FLASK SETUP==========================================================================================================
----------------------------------------__init__.py-------------------------------------------------
-Import flask in __init__.py (from flask import flask)
-Create function and initalize the flask app (def create app(): app = flask(__name__))
-Add secret key (app.config["SECRET_KEY"] = "dsjfsoifio" -> secures cookies
-return application from func (return app)
--------------------------------------------Main.py------------------------------------------
-import the __init__ to main python function (from website import create_app)
-Run the app and set debug to True since it will auto refresh(app = create_app(), if __name__ = '__main__': app.run(debug=True))
==================================================================================BLUEPRINT SETUP==========================================================================================================
--------------------------------------------Views.py------------------------------------------
import flask with blueprint(from flask import Blueprint) -> a way of definining and sectioning urls 
-Create a variable with blueprint (views = Blueprint('views (name of the blueprint)'), __name__) -> To let flask know where youre running it 
--------------------------------------------Auth.py------------------------------------------
Do the same above for auth.py  
--------------------------------------------Views.py------------------------------------------
-Add route (URL directory) (@views.route('/'))
-Add a function (def home(): return "")
----------------------------------------__init__.py-------------------------------------------------
-Import the views.py (the blueprint?) to create app (from .views import views) an auth.
-Register the blue print (app.register_blueprint(views, url_prefix="/")) (app.register_blueprint(auth, url_prefix="/")) -> the prefix is for directory -> "/" is home
--------------------------------------------Auth.py------------------------------------------
-Create route (@auth.route('/login')) and function (def login(): return "")
-Create route (@auth.route('/logout')) and function (def logout(): return "")
-Create route (@auth.route('/sign-up')) and function (def sign_up(): return "")
=================================================================================JINJA TEMPLATE HTML SETUP===================================================================================================================================
--------------------------------------------Base.html (template) (created)------------------------------------------
-Create html skeleton (!doctype)
-Use Jinja for templating (<title>{% block title %}Home{% endblock %}</title>) -> "title" can be named anything (child template will override it upon adding {% block title%})
#Note that adding js into file is <script> type = "js", src="{{url_for('static', filename= index.js')}}" (not neeeded because this is a python module)
-Add navbar
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbar"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbar">
        <div class="navbar-nav">
          <a class="nav-item nav-link" id="home" href="/">Home</a>
          <a class="nav-item nav-link" id="logout" href="/logout">Logout</a>
          <a class="nav-item nav-link" id="login" href="/login">Login</a>
          <a class="nav-item nav-link" id="signUp" href="/sign-up">Sign Up</a>
        </div>
      </div>
    </nav>
--------------------------------------------home.html (created)------------------------------------------
-Use inheritance {% extends "base.html" %} (gets all the html elements and css from there)
-override the set block proeprties aka block title ({% block title %}Changed{% endblock %})
--------------------------------------------views.py------------------------------------------
-Render the template from home.html -> def home(): render_template("home.html") -? stuck to the blueprint and will be registered
--------------------------------------------Base.html (template)------------------------------------------
-Add content under the nav -> (<div>{% block content %} {%endblock%}</div>)
--------------------------------------------home.html------------------------------------------
-Override block content with content {% block content %} <h1>This is the home page</h1>{%endblock%}
--------------------------------------------login.html (created) ------------------------------------------
-Use inheritance {% extends "base.html" %} (gets all the html elements and css from there)
-Override block content with {% block content %} <h1>This is the login page</h1>{%endblock%}
--------------------------------------------sign-up.html (created)------------------------------------------
-Use inheritance {% extends "base.html" %} (gets all the html elements and css from there)
-Override block content with content {% block content %} <h1>This is the sign up page</h1>{%endblock%}
--------------------------------------------Auth.py------------------------------------------
Modify function from (def login(): return "") to (def login(): return rendeer_template(login.html))
Modify function from (def logout(): return "") to (def logout(): return "Null")
Modify function from (def sign_up(): return "") ti (def sign-up(): return render_template(signup.html)
#Note: Putting render_template(login.html, yes="variable"), you can access the variable in the template
use in login.html -> {{yes}} (you can also write an if statemment)
--------------------------------------------sign-up.html (created)------------------------------------------
-Add form with confirmation of password, email and name
<form method="POST">
<label for="email">Email address </label>
<input type = "email" id = "email" name = "email" placeholder="Enter Email"> -> local host will receive a thing like email : [fill in stuff]
<label for="firstName">Name</label>
<input type = "text" id = "name" name = "name" placeholder="Enter Name">
<label for="password1">Password</label>
<input
  type="password"
  class="form-control"
  id="password1"
  name="password1"
  placeholder="Enter password"
/>
<label for="password2">Password (Confirm)</label>
<input
  type="password"
  class="form-control"
  id="password2"
  name="password2"
  placeholder="Confirm password"
/>
<br />
<button type="submit" class="btn btn-primary">Submit</button>
</form>
--------------------------------------------login.html (created)------------------------------------------
<form method="POST">
<label for="email">Email address </label>
<input type = "email" id = "email" name = "email" placeholder="Enter Email"> -> local host will receive a thing like email : [fill in stuff]
<label for="password">Password</label>
<input
  type="password"
  class="form-control"
  id="password"
  name="password"
  placeholder="Enter password"
/>

<br />
<button type="submit" class="btn btn-primary">Login</button>
</form>

================================================================================Accepting Requests and verifications===================================================================================================================================
----------------------------------------auth.py-------------------------------------------------
-Add the avaliable methods the route can use (auth.route('/login', methods['GET', 'POST'])) -> Since the method of the form is POST request (Can accetp post now)
-Import request from flask (from flask import request)
#Note you need to differentiate to accept POST only as GET request will be sent on reload without pressing submit button, therefore you need to reject it 
-print request.data -> gets key/data attribute from the route itself
-Only accept POST request in sign_up page (auth) (if request.method == "POST": email = request.form.get('email'), firstname = request.form.get('firstname'), password1 = request.form.get('password1'), password2 = request.form.get('password2'))
#Note request.form.get(x) is retrieving POST data from a specific input where x is the name attribute in the html template
===============================================================================Flashing messages====================================================================================================================================
import flask from flask (from flask import flash)
-Add checks (if len(email) < 4: do something, 
  if len(firstname < 2: do something)
    if (password1 != password2: do something)

sign_up():
.
.
-flash a message in if statement (if len(email) < 4: flash('Email must be greater than 4 characters.', category= 'error') -> cateogirsation and organsiation
if len(firstName) < 2: flash('First name must be greater than 1 characters.', category= 'error')
.
.
.
    else: 
      flash('account created', category='success')
----------------------------------------base.html-------------------------------------------------
-> under nav 
-1)Get all the flashed messages
-2)check if there's even any messages' 
-3) loop through the avaliable messages and the category itself
-4) add messages 
-5) If statemeents to differeniate between the success and error messages
1){ % with messages = get_flashed_messages(with_categories=true) %}     #get all the flash messages with  categories ('success', 'error')
2) {% if messages %}
3){% for category, message in messages %}
5) {% if category == "success" %}
4) <div> {{ message }}</div>
5) {% else %}
<div> {{message }}</div>
{% endif %}

{% endfor %}
{% endif %}
{% endwith %}
===========================================================Database Initalization========================================================================================================================================================
----------------------------------------__init__.py-------------------------------------------------
-Import flask_sqlalchemy (from flask_sqlalchemy import SQLAlchemy)
-Initalize database (db = SQLAlchemy())
-Give database file a name (DB_NAME = "database.db")
- Tell flask that we are using this database and where is it lcoated (app.config['SQLALCHEMY_DATBASE_URI'] = f"sqllite:///{DB_NAME}") <- show location
-Initalize database (let db know which app) (db.init_app(app))
                    |
                sqlalchemy()
===========================================================Database Creation========================================================================================================================================================

----------------------------------------models.py------------------------------------------------- (Create database)

-Import the database init which is db=SQLALCHEMY() (from website import db)
-Import flask login and userMixin (from flask_login import UserMixin)

-Create a user class (like a user accout)  -> db.Model is the base class #my theory is adding a column for a section of the user 
class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True) -> Integer is the datatype and primary_key is a unique identifier that represents th object (say if both have the same name)
  email = db.column(db.String(150), unique=True) -> Max length. Unique = T rue is no user could have the same thing
  password = db.Column(db.String(150))
  first_name = db.Column(db.String(150))

-Create a Note class
class Note(db.Model): #I assume that the reason because it crashes when I remove this is because the genereal model fo the databaes has been already set up
  id = db.Column(db.Integer, primary_key=True)
  data = db.Column(db.String(10000))
  date = db.Column(db.DateTime(timezone=True), default = func.now()) -> Check the timezone and chekc the current time

  -Associate Note to user, for each user account (user_id = db.Column(db.Integer, db.ForeignKey('user.id')))
  foreign_key referneces the column of another database and must pass a valid id of an existing user to the column (one to many relationshiop)
  -> User.id >> in SQL User class wiill become user and .id is referencing the id of the user class

  -Add notes relationship (db.relationship('Note'))
===========================================================Database Connection========================================================================================================================================================
  ----------------------------------------__init__.py-------------------------------------------------
  Import models (import .models) (after register blue print before return app)
  -add another function (def create_database(app)) _> func so that it will create databse if we don't have it and if we have it' we will skip it since we don't wnat to override the databse'
  -Import path module (from os import path)
  -in create_database(app) (if not path.exists('website/' + DB_NAME): db.create_all(app=app); ) app = app tells where to use the databse
  ======================================================Adding users and logging in users (with redirection to pages)=============================================================================================================================================================
  ----------------------------------------auth.py-------------------------------------------------
  -Import User class from models
  -Import db from . import db
  -Import hash algo (from werzberg.security import generate_passoword_has, check_password_hash)
-Create new user (under sign up func in the else:) (new_user = User(email = email, firstName = firstName, password=generate_password_hash(password1, method="sha256")))
-Add account to database (db.session.add(new_user))
-Update the changes (db.session.commit())
-Import redirect url_for (from flash import redirect, url_for)
-return a redirection to the homepage after valid acciont was created (return redirect(url_for('views.home'))) -> views meaning from the file and .home is the template itself


in login func:
-check if the request is post (if request.method == "POST")
-get the email and passwrod from the user input in the if statement -> (email = request.form.get('email'), request.form.get('password'))
-filter to email take the first result (user = User.query.filter_by(email=email).first())
-have an if statement to say if  there is a user 
if user:
  if check_password_hash(user.password,password):
    flash ('logged in successfully!', category = 'success')
    return redirect(url_for('views.home'))
  else:
    flash('incorrect password, try again.', cateogry= 'error')
else:
  flash(
    "email does not exist.", category = "error"
  )


in signup func:
user = User.query.filter_by(email=email).first()
if user:
  flash('"email already exissts', category='Error')
    ==========================================================Flask login module shit=========================================================================================================================================================
  ----------------------------------------auth.py-------------------------------------------------
  import flask login (from flask_login import login_user, login_required, logout_user, current_user)
  in login func:
  login_user(user, remember=True) -> r emember it untnil it doesn't store the session'

  in logout func:
  return redirect(url_for('auth.login'))

  below auth.route('/logout')
  @login_required - > makes sure this one needs login
  ----------------------------------------views.py-------------------------------------------------
    import flask_login
    -require login required 
 ----------------------------------------__init__.py-------------------------------------------------
  - under create_app(): and below user,note
  login_manager = LoginManager()
  login_manager.login_view = 'auth.login' -> where should the user go if the user is not logged in
  login_manager.init_app(app) -> initliaze where to go
  @login_manager.user_loader
  def load_user(id):
    return User.query.get(int(id)) - > usedto reference the loading of users 
 ----------------------------------------views.py-------------------------------------------------
 r