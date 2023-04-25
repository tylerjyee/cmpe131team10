from flask import render_template, redirect, flash, url_for, request
from .forms import LoginForm, ContactForm, ComposeForm, RegisterForm
from app import myapp_obj
from flask_login import current_user, login_user, logout_user, login_required
#from flask_mail import Mail, Message

@myapp_obj.route("/")
def welcome():
    return render_template('welcome.html')

@myapp_obj.route("/home")
def home():
    return render_template('home.html')

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
        return redirect('/home.html')
    return render_template('login.html', form=form)

@myapp_obj.route("/register", methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'You have successfully registered')
        return redirect('/home.html')
    return render_template('register.html', form=form)

@myapp_obj.route('/todo', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        # Get the todo item from the form input
        todo_item = request.form.get('todoitem')
        # Add the todo item to the database or file
        # Redirect back to the todo page to show the updated list
        with open("todo.txt", "a") as f:
            f.write(todo_item + "\n")
        # Redirect back to the todo page to show the updated list
        return redirect(url_for('/todo'))

    # Get the todo list from the database or file
    with open("todo.txt", "r") as f:
        todo_list = f.readlines()
    # Render the todo page with the todo list
    return render_template('todo.html', todo_list=todo_list)


@myapp_obj.route('/emails', methods = ['GET','POST'])
def emails():
    form = ComposeForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields required')
            return render_template('emails.html', form=form)
        else:
            print('Email Sent')
            return redirect('/home.html')
    elif request.method == 'GET':
        return render_template('emails.html', form=form)

@myapp_obj.route('/contacts', methods = ['GET','POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields required')
            return render_template('contacts.html', form=form)
        else:
            return 'form posted'
    elif request.method == 'GET':
        return render_template('contacts.html', form=form)
    
@myapp_obj.route("/profile")
def profile():
    return render_template('profile.html')