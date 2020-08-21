from flask import Blueprint

notebooks = Blueprint('notebooks', __name__)

from . import routes