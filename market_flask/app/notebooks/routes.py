from flask import render_template
from ..models import Product
from . import notebooks
from .. import db


@notebooks.route('/')
def index():
    products = Product.query.all()
    return render_template('notebooks.html', products=products, quantity=len(products))


@notebooks.route('/<int:id>')
def personal(id):
    product = Product.query.get(id)
    return render_template('product.html', product=product)

