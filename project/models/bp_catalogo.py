from project import db
#from project.models.bp_upload import Image


rubro_producto = db.Table('rubro_producto',
                        db.Column('rubro_id', db.Integer, db.ForeignKey('rubros.id')),
                        db.Column('producto_id', db.Integer, db.ForeignKey('productos.id'))
                        )



productor_producto = db.Table('productor_producto',
                        db.Column('productor_id', db.Integer, db.ForeignKey('productores.id')),
                        db.Column('producto_id', db.Integer, db.ForeignKey('productos.id'))
                        )



class Productor(db.Model):

    __tablename__ = 'productores'

    id = db.Column(db.Integer, primary_key=True)
    nombre_fantasia = db.Column(db.String, nullable=False)
    razon_social = db.Column(db.String, nullable=False)
    website = db.Column(db.String)
    productos = db.relationship('Producto', secondary= productor_producto, back_populates='productores')
    imagenes = db.relationship('Imagen', back_populates='productor')

    def __init__(self, nombre_fantasia, razon_social, website=None):
        self.nombre_fantasia = nombre_fantasia
        self.razon_social = razon_social
        self.website= website

    def __repr__(self):
        return '<Productor {}>'.format(self.nombre_fantasia)
    

class Producto(db.Model):

    __tablename__ = 'productos'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(60), nullable=False)
    productores = db.relationship('Productor', secondary= productor_producto, back_populates='productos')
    rubros = db.relationship('Rubro', secondary = rubro_producto, back_populates = 'productos')

    def __init__(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        return '<Producto: {}>'.format(self.nombre)



class Rubro(db.Model):

    __tablename__ = 'rubros'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(60), nullable=False)
    productos = db.relationship('Producto', secondary= rubro_producto, back_populates='rubros')

    def __init__(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        return '<Rubro: {}>'.format(self.nombre)

