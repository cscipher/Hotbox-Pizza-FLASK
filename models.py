from . import db
from flask_login import UserMixin


class place_order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Fname = db.Column(db.String(20),nullable=False)
    mailid = db.Column(db.Text, nullable=False)
    num = db.Column(db.Integer, nullable=False)
    address = db.Column(db.Text, nullable=False)
    deltype = db.Column(db.Text, nullable=False)
    ing = db.Column(db.Text, nullable=False)
    crust = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)


class contactus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name_d = db.Column(db.String(30), nullable=False)
    email_d = db.Column(db.Text, nullable=False)
    query_d = db.Column(db.Text, nullable=False)


class user_val(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def is_active(self):
        return True

    def get_id(self):
        return self.email

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False


