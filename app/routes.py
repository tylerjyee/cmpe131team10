from flask import render_template
from flask import redirect
from flask import flash
from flask import url_for
from .forms import LoginForm
from app import myapp_obj
from flask_login import current_user, login_user, logout_user, login_required

@myapp_obj.route("/", methods=["GET"])
def to_home():
    return redirect(url_for('home'))

@myapp_obj.route("/home")
def home():
    return render_template('home.html', title = "home")

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

@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    title = "Login Page"
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Login invalid username or password!')
            return redirect('/login')

        login_user(user, remember=form.remember_me.data)
        flash(f'Successfull Login for requested user {form.username.data} at {time.strftime("%H:%M:%S")}')
        return redirect('/')

    return render_template("login.html", form=form,title=title)

@myapp_obj.route("/register")
def register():
    return render_template('register.html')

@myapp_obj.route("/todo")
def todo():
    return render_template('todo.html',)

@myapp_obj.route("/emails")
def emails():
    return render_template('emails.html')

@myapp_obj.route("/contacts")
def contacts():
    return render_template('contacts.html')



"""
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

@myapp_obj.route("/members/<string:name>/")
def getMember(name):
    return escape(name)


@myapp_obj.route("/compose")
@login_required
def compose():
    return render_template('compose.html')"""