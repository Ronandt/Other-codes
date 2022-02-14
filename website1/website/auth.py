from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user, current_user #use usermxin to use currentuser
from werkzeug.security import generate_password_hash,  check_password_hash #hashing password
auth = Blueprint('auth', __name__)

@auth.route("/login", methods=["GET", "POST"]) #https://flask.palletsprojects.com/en/2.0.x/quickstart/
def login():
    data = request.form #get info from what is sent
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get('password')
        user = User.query.filter_by(email = email).first() #filter those who have this email
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category="success")
                login_user(user, remember=True) #store in the flask session if the web server is running
                return redirect(url_for('views.home')) 
            else:
                flash("Incorrect password, try again.", category="error") #access passwrod, remember classes and check classess
        else:
            flash("Email does not exist", category = "error")
    return render_template("login.html", text="Testing", boolean=True, methods = ['GET', 'POST'], user=current_user)

@auth.route("/logout") #equivalent to logout =  auth.route("/logout")(logout)
@login_required #cannot access this page unless the user is logged in
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route("/sign-up", methods = ['GET', 'POST'])
def sign_up():
    if request.method=="POST": #https://stackoverflow.com/questions/4497643/refreshing-a-page-in-a-browser-yields-post-or-get-request
        email = request.form.get("email")
        password1  = request.form.get("password1")
        password2 = request.form.get('password2')
        user = User.query.filter_by(email = email).first() #prevents same email
        print(user)
        if user:
            flash("Email already exists", category="error")
        elif len(email) < 4:
            flash("Email must be greater than 3 characters", category ="error" )#just organistation for category)
        elif password1 != password2:
            flash("Password must be equal to the confirmation", category ="error" )
        else:
            new_user = User(email = email, password=generate_password_hash(password1, method="sha256"))
            db.session.add(new_user) #add user
            db.session.commit() #made changes into the database, upate it
            login_user(new_user, remember=True) 

            flash("Account created!", category="success")
            return redirect(url_for('views.home')) #redirect to the thing
    return render_template("signup.html", user=current_user)