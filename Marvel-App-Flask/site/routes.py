from flask import Blueprint, render_template
from flask_login import login_user, logout_user, current_user, login_required

site = Blueprint('site', __name__, template_folder='site_templates')


@site.route('/')
def home():
    return render_template("index.html")


@site.route('/profile')
@login_required
def profile():
    return render_template("profile.html")


@site.route('/bye')
def bye():
    return render_template("bye.html")