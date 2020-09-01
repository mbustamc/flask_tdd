from project import db


class Imagen(db.Model):
    __tablename__ = "imagenes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64))
    path = db.Column(db.Unicode(128))
    productor_id = db.Column(db.Integer, db.ForeignKey('productores.id'), nullable=True)
    productor = db.relationship('Productor', back_populates='imagenes')

    def __unicode__(self):
        return self.name