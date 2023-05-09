from flask import render_template, redirect, flash, url_for, session, request


from .forms import EditProfileForm, LoginForm, ContactForm, ComposeForm, RegisterForm, UnregisterForm, ForgotpwForm, TodoForm, StartChatForm
from .models import ChatRoom, User, ToDoList

from app import myapp_obj, db
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
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
        user=User.query.filter_by(username=form.username.data).first()
        # check the password and if password matches
        try:
            if form.username.data==user.username and form.password.data==user.password:
                # login_user(user)
                #flash(f'Here are the input {form.username.data} and {form.password.data}')
                flash(f'Login successful for {form.username.data}')
                return redirect(url_for('home'))
        except AttributeError:
        #if password doesn't match
            flash(f'Login unsuccessful. Please try again')
            #return redirect(url_for('login'))
    return render_template('login.html', form=form)


@myapp_obj.route("/register", methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user=User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'You have successfully registered for {form.username.data} and {form.email.data}')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@myapp_obj.route("/unregister", methods=['GET','POST'])
def unregister():
    form = UnregisterForm()

    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        if form.username.data==user.username and form.email.data==user.email and form.password.data==user.password:
            db.session.delete(user)
            db.session.commit()
            flash(f'Successfully deleted an account for {form.username.data}')
            return redirect(url_for('login'))
        #if password doesn't match
        else:
            flash(f'Unsuccessful deleting an account for {form.username.data}. Please try again')
            return redirect(url_for('unregister'))

    return render_template('unregister.html', form=form)

@myapp_obj.route('/todo', methods=['GET', 'POST'])
def todo():
    #cretes to-do list form
    form = TodoForm()
    title = "To-Do List"
    #trys to create a new task on todo lists
    if request.method == 'POST':
        task_content = request.form['taskname']
        new_task = ToDoList(task_name = task_content)
        try:
            #adds new task
            db.session.add (new_task)
            db.session.commit()
            return redirect('To-do List')
        except:
            return flash ('Task could not be added')
    else:
        tasks = todo.query.all()
        return render_template ("todolist.html", tasks = tasks, form=form, title=title)
    
@myapp_obj.route('/delete/<int:id>')
def delete(id):
    delete_task = ToDoList.query.get_or_404(id)
    try:
        db.session.delete(delete_task)
        db.session.commit()
        return redirect ('/todo')
    except:
        return flash ('Error: could not delete a task')

@myapp_obj.route ('/update/<int:id>', methods = ['GET', 'POST'])
def update(id):
    form = TodoForm()
    title = "Update Task"
    task = ToDoList.query.get_or_404(id)
    if request.method == 'POST':
        task.task_name = request.form['task_name']
        try:
            db.session.commit()
            return redirect ('/todo')
        except:
            return flash('Error: could not update a task')
    else:
        return render_template('update.html', task = task, form=form,title=title)
 
@myapp_obj.route('/start_chat', methods=['GET', 'POST'])
def start_chat():
    form = StartChatForm()
    if form.validate_on_submit():
        # get the username of the person to chat with
        chat_with = form.chat_with.data
        # create a chat room with the current user and the person to chat with
        chat_room = current_user.username + '-' + chat_with
        # redirect to the chat room
        return redirect(url_for('chat_room', room=chat_room))
    # get a list of all users except the current user
    users = User.query.filter(User.username != current_user.username).all()
    return render_template('startchat.html', form=form, users=users)

@myapp_obj.route('/delete_chat/<room>', methods=['POST'])
def delete_chat(room):
    # ensure that the current user is part of the chat room
    if current_user.username in room:
        # delete the chat room
        chat_room = ChatRoom.query.filter_by(name=room).first()
        db.session.delete(chat_room)
        db.session.commit()
        # redirect to the home page
        return redirect(url_for('home'))
    else:
        # if the current user is not part of the chat room, return an error message
        flash('You do not have permission to delete this chat room.')
        return redirect(url_for('home'))
    
@myapp_obj.route('/emails', methods = ['GET','POST'])
def emails():
    return render_template('emails.html')
    
@myapp_obj.route("/compose", methods = ['GET','POST'])
def compose():
    form = ComposeForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields required')
            return render_template('compose.html', form=form)
        else:
            print('Email Sent')
            return redirect('/emails')
    elif request.method == 'GET':
        return render_template('compose.html', form=form)

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
    
@myapp_obj.route("/editprofile", methods = ['GET','POST'])
def profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('profile'))
    return render_template('editprofile.html', form=form)

@myapp_obj.route("/profile", methods=['GET','POST'])
def viewprofile():
    return render_template('profile.html')

@myapp_obj.route("/forgotpw", methods=['GET','POST'])
def forgotpw():
    #form = ForgotpwForm()
    #if form.validate_on_submit():
    #    flash(f'You have successfully reset your password')
    #    return redirect('/home')
    #return render_template('forgotpw.html', form=form)

    form = ForgotpwForm()
    # if form inputs are valid
    if form.validate_on_submit():
        # search database for username and email
        # user = User.query.filter_by(...)
        user=User.query.filter_by(username=form.username.data).first()
        # check the password and if password matches
        if form.username.data==user.username and form.email.data==user.email:
    
            flash(f'This is your password: {user.password}')
            return redirect(url_for('forgotpw'))
        else:
            flash(f'Not registed account! Please try again')
            return redirect(url_for('forgotpw'))
    return render_template('forgotpw.html', form=form)
