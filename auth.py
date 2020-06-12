from flask import Blueprint, url_for, render_template , request, redirect
from .models import user_val
from . import db
from flask_login import login_user, login_required, logout_user

auth = Blueprint('auth',__name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        semail = request.form.get('getmail')
        passw = request.form.get('getpass')

        user = user_val.query.filter(user_val.email==semail).first()
        check_pass = db.session.query(user_val.password).filter(user_val.email == semail).first()
        
        
        if user:
            login_user(user)
            return render_template('login.html', checkpass=check_pass, inputpass=passw)
        else:
            return render_template('login.html', checkpass=check_pass, inputpass=passw)
        
    else:
        
        return render_template('login.html',checkpass=None)



@auth.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method=='POST':
        fname = request.form.get('first name')
        lname = request.form.get('last name')
        semail = request.form.get('email')
        password = request.form.get('passwordget')
    
        user = user_val.query.filter_by(email=semail).first()
        if not user:
            new_signup = user_val(first_name=fname, last_name=lname, email=semail, password=password)
            db.session.add(new_signup)
            db.session.commit()
            return redirect('/login')
        else:
            return render_template('signup.html',checkmail=user, inputmail=semail)
       
    else:
        user,semail = None, None
        return render_template('signup.html',checkmail=user, inputmail=semail)




@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect('/')
