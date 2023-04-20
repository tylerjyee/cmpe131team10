from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField 
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Userename', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
class ContactForm(FlaskForm):
   name = StringField("Name", validators=[DataRequired()])
   email = StringField("Email", validators=[DataRequired()])
   subject = StringField("Subject", validators=[DataRequired()])
   message = TextAreaField("Message")
   submit = SubmitField("Send") 

