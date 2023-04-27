from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(32), unique=True)
    email = db.Column(db.String(128), unique=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<user {self.id}: {self.username}:{self.email}>'

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class ToDoList(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name_of_task = db.Column(db.String(100))
    completed_form = db.Column(db.Boolean)



