from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField 
from wtforms.validators import DataRequired, Email, Length
class LoginForm(FlaskForm):
    username = StringField('Userename', validators=[DataRequired(), Length(min=3)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
class ContactForm(FlaskForm):
   name = StringField("Name", validators=[DataRequired()])
   email = StringField("Email", validators=[DataRequired()])
   subject = StringField("Subject", validators=[DataRequired()])
   message = TextAreaField("Message", validators=[DataRequired()])
   submit = SubmitField("Send")

class ComposeForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    subject = StringField("Subject", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send")


class RegisterForm(FlaskForm):
    email = StringField('Enter an email', validators=[DataRequired(), Email(message='Invalid email'),Length(max=50,min=3)])
    username = StringField('Enter an username', validators=[DataRequired(), Length(max=15,min=3)])
    password = PasswordField('Enter a new password', validators=[DataRequired(), Length(max=20,min=3)])
    password2 = PasswordField('Re-enter the password', validators=[DataRequired(), Length(max=20,min=3)])
    register = SubmitField('Register')
    cancel = SubmitField('Cancel')

class TodoForm(FlaskForm):
    todoitem = StringField("To-Do Item", validators=[DataRequired()])
    text = TextAreaField("Text.", validators=[DataRequired()])
    cancel = SubmitField('Cancel')

class StartChatForm(FlaskForm):
    chat_with = StringField('Chat With', validators=[DataRequired()])
    submit = SubmitField('Start Chat')

class DeleteChatForm(FlaskForm):
    submit = SubmitField('Delete Chat')