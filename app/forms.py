from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField 
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Userename', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
class ContactForm(FlaskForm):
   name = StringField("Name")
   email = StringField("Email")
   subject = StringField("Subject")
   message = TextAreaField("Message")
   submit = SubmitField("Send") 

