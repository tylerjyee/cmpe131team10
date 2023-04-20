from flask import render_template, redirect, flash, url_for, request
from .forms import LoginForm, ContactForm
from app import myapp_obj
from flask_login import current_user, login_user, logout_user, login_required

@myapp_obj.route("/")
@myapp_obj.route("/index.html")
def index():
    name = 'Carlos'
    books = [ {'author': 'authorname1',
                'book':'bookname1'},
             {'author': 'authorname2',
              'book': 'bookname2'}]
    return render_template('hello.html',name=name, books=books)

@myapp_obj.route("/hello")
@login_required
def hello():
    return "Hello World!"

@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    # create form
    form = LoginForm()
    # if form inputs are valid
    if form.validate_on_submit():
        # search database for username
        # user = User.query.filter_by(...)
        # check the password
        # if password matches
        # login_user(user)
        flash(f'Here are the input {form.username.data} and {form.password.data}')
        return redirect('/')
    return render_template('login.html', form=form)

@myapp_obj.route("/register")
def register():
    return render_template('register.html')

@myapp_obj.route("/todo")
def todo():
    return render_template('todo.html',)

@myapp_obj.route("/emails")
def emails():
    return render_template('emails.html')

@myapp_obj.route("/emails")
def emails():
    return render_template('emails.html')

@myapp_obj.route('/contacts', methods = ['GET','POST'])
def contact():
    form = ContactForm()
    return render_template('contacts.html', form = form)