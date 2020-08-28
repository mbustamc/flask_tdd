from project import db



productor_rubro = db.Table('productor_rubro',
                        db.Column('productor_id', db.Integer, db.ForeignKey('productores.id')),
                        db.Column('rubro_id', db.Integer, db.ForeignKey('rubros.id'))
                        )

class Productor(db.Model):

    __tablename__ = 'productores'

    id = db.Column(db.Integer, primary_key=True)
    nombre_fantasia = db.Column(db.String, nullable=False)
    razon_social = db.Column(db.String, nullable=False)
    website = db.Column(db.String)
    rubros = db.relationship('Rubro', secondary= productor_rubro, back_populates='productores')

    def __init__(self, nombre_fantasia, razon_social, website=None):
        self.nombre_fantasia = nombre_fantasia
        self.razon_social = razon_social
        self.website= website

    def __repr__(self):
        return '<Productor {}>'.format(self.nombre_fantasia)
    

class Rubro(db.Model):

    __tablename__ = 'rubros'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(60), nullable=False)
    productores = db.relationship('Productor', secondary= productor_rubro, back_populates='rubros')

    def __init__(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        return '<Rubro: {}>'.format(self.nombre)
