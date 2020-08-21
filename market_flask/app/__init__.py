import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

db = SQLAlchemy()
admin = Admin()

def create_app(config_name):
	
	app = Flask(__name__)

	# import configuration
	cfg = os.path.join(os.getcwd(), 'config', config_name + '.py')
	app.config.from_pyfile(cfg)

	# initialize extensions
	db.init_app(app)
	admin.init_app(app)

	with app.app_context():
		from .models import Product, Year, Brand, Specification ,Screen, Processor, Memory, Storage, Image
		admin.add_view(ModelView(Product, db.session()))
		admin.add_view(ModelView(Year, db.session()))
		admin.add_view(ModelView(Brand, db.session()))
		admin.add_view(ModelView(Specification, db.session()))
		admin.add_view(ModelView(Screen, db.session()))
		admin.add_view(ModelView(Processor, db.session()))
		admin.add_view(ModelView(Memory, db.session()))
		admin.add_view(ModelView(Storage, db.session()))
		admin.add_view(ModelView(Image, db.session()))

	# import blueprints
	from .notebooks import notebooks as notebooks_blueprint
	app.register_blueprint(notebooks_blueprint, url_prefix='/notebooks')

	return app