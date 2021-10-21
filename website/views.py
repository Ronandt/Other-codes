from flask import Blueprint, render_template #blueprint basically a buncb of url and a way to seperate files
views = Blueprint('views', __name__) #  To put simply, in the Router you determine what should happen when a user visits a certain page. (Naviagation?)
#Second argument of blueprint is blueprints import name, helps locate blueprint resources
#First argument is to define the name of the blueprint
from flask_login import login_required, current_user
@views.route('/') #whatever the route is going to be 
@login_required #requires login
def home(): #function will run whenever we go to '/' route
    return render_template("home.html", user=current_user) #render html
    
