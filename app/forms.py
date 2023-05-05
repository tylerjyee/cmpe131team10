from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField 
from wtforms.validators import DataRequired, Email, Length, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Userename', validators=[DataRequired(), Length(min=3)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')
    
class ContactForm(FlaskForm):
   name = StringField("Name", validators=[DataRequired()])
   email = StringField("Email", validators=[DataRequired()])
   subject = StringField("Subject", validators=[DataRequired()])
   message = TextAreaField("Message", validators=[DataRequired()])
   submit = SubmitField("Send")

class ComposeForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    subject = StringField("Subject", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send")


class RegisterForm(FlaskForm):
    email = StringField('Enter an email', validators=[DataRequired(),Length(max=50,min=3),Email(message='Invalid email')])
    username = StringField('Enter an username', validators=[DataRequired(), Length(max=15,min=3)])
    password = PasswordField('Enter a new password', validators=[DataRequired(), Length(max=20,min=3)])
    password2 = PasswordField('Re-enter the password', validators=[DataRequired(), EqualTo('password'), Length(max=20,min=3)])
    register = SubmitField('Register')


class UnregisterForm(FlaskForm):
    email = StringField('Enter email', validators=[DataRequired(),Email(message='Invalid email'),Length(max=50,min=3)])
    username = StringField('Enter username', validators=[DataRequired(), Length(max=15,min=3)])
    password = PasswordField('Enter password', validators=[DataRequired(), Length(max=20,min=3)])
    password2 = PasswordField('Re-enter the password', validators=[DataRequired(),EqualTo('password'), Length(max=20,min=3)])
    unregister = SubmitField('Unregister')

class ForgotpwForm(FlaskForm):
    username = StringField('Enter username', validators=[DataRequired(), Length(max=15,min=3)])
    email = StringField('Enter email', validators=[DataRequired(),Length(max=50,min=3)])
    submit = SubmitField('Submit')

class TodoForm(FlaskForm):
    todoitem = StringField("To-Do Item", validators=[DataRequired()])
    text = TextAreaField("Text.", validators=[DataRequired()])
    cancel = SubmitField('Cancel')

class StartChatForm(FlaskForm):
    chat_with = StringField('Chat With', validators=[DataRequired()])
    submit = SubmitField('Start Chat')

class DeleteChatForm(FlaskForm):
    submit = SubmitField('Delete Chat')

class EditProfileForm(FlaskForm):
    username = StringField("Name", validators=[DataRequired()])
    submit = SubmitField('Submit')