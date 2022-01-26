from flask import render_template
from app import app
from models.customer_orders import customer_orders

@app.route('/orders')
def index():
    return render_template('index.html', customer_orders=customer_orders)

@app.route('/orders/<customer_i>')
def get_single_order(customer_i):
    customer_i = int(customer_i)
    return render_template('order.html', customer_orders=customer_orders[customer_i])