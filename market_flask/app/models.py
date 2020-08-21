from . import db


class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    file = db.Column(db.String)
    products = db.relationship('Product', backref='image', lazy='dynamic')

    def __repr__(self):
        return f'{self.file}'


class Year(db.Model):
    __tablename__ = 'years'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.String)
    products = db.relationship('Product', backref='year', lazy='dynamic')

    def __repr__(self):
        return f'{self.year}'


class Brand(db.Model):
    __tablename__ = 'brands'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brand = db.Column(db.String)
    products = db.relationship('Product', backref='brand', lazy='dynamic')

    def __repr__(self):
        return f'{self.brand}'


class Screen(db.Model):
    __tablename__ = 'screens'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    screen = db.Column(db.String)
    specifications = db.relationship('Specification', backref='screen', lazy='dynamic')

    def __repr__(self):
        return f'{self.screen}'


class Processor(db.Model):
    __tablename__ = 'processors'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    processor = db.Column(db.String)
    specifications = db.relationship('Specification', backref='processor', lazy='dynamic')

    def __repr__(self):
        return f'{self.processor}'


class Memory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    memory = db.Column(db.String)
    specifications = db.relationship('Specification', backref='memory', lazy='dynamic')

    def __repr__(self):
        return f'{self.memory}'


class Storage(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    storage = db.Column(db.String)
    specifications = db.relationship('Specification', backref='storage', lazy='dynamic')

    def __repr__(self):
        return f'{self.storage}'


class Specification(db.Model):
    __tablename__ = 'specifications'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    processor_id = db.Column(db.Integer, db.ForeignKey(Processor.id))
    screen_id = db.Column(db.Integer, db.ForeignKey(Screen.id))
    memory_id = db.Column(db.Integer, db.ForeignKey(Memory.id))
    storage_id = db.Column(db.Integer, db.ForeignKey(Storage.id))
    products = db.relationship('Product', backref='spec', lazy='dynamic')
    

    def __repr__(self):
        return f'{self.screen}, {self.processor}, {self.memory}, {self.storage}'


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price = db.Column(db.String)
    year_id = db.Column(db.Integer, db.ForeignKey(Year.id))
    spec_id = db.Column(db.Integer, db.ForeignKey(Specification.id))
    brand_id = db.Column(db.Integer, db.ForeignKey(Brand.id))
    image_id = db.Column(db.Integer, db.ForeignKey(Image.id))