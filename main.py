from flask import Blueprint, render_template , redirect, request
from flask_login import login_required, current_user
from .models import contactus, place_order, user_val
from . import db


main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('homepage.html')


@main.route('/place_order', methods=['POST','GET'])
@login_required
def order():
    o_ing_str = ''
    if request.method == 'POST':     
        order_Fname = request.form.get('name')
        order_mailid = request.form.get('mail')
        order_num = request.form.get('mob')
        order_address = request.form.get('address')
        order_deltype = request.form.get('inlineRadioOptions')
        order_ing = request.form.getlist('chkoption')
        o_ing_str = ', '.join(i for i in order_ing)
        order_crust = request.form.get('crs')
        order_size = request.form.get('size')
        new_order = place_order(Fname=order_Fname, mailid=order_mailid, num=order_num, address=order_address, deltype=order_deltype, ing=o_ing_str, crust=order_crust, size=order_size)
        db.session.add(new_order)
        db.session.commit()
        return render_template('place_order.html', confirm=True)
    else:
        return render_template('place_order.html')




@main.route('/contact', methods=['GET', 'POST'])
@login_required
def query():
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        query = request.form.get('query')
        email1 = request.form.get('email_q')
        new_query = contactus(full_name_d=full_name, query_d=query, email_d=email1)
        db.session.add(new_query)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('contactus.html')
