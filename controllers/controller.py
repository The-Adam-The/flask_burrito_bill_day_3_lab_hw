from flask import render_template
from app import app
from models.customer_orders import customer_orders

@app.route('/orders')
def index():
    return render_template('index.html', customer_orders=customer_orders)