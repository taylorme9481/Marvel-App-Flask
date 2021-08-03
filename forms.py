from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskForm):
    #email, pw, submit
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),])
    submit_button = SubmitField()



def find(n, array):
    middle = len(array) // 2
    print(middle)

    return n > array[middle]