#!/usr/bin/env python
# -*- coding: utf-8 -*-

from project import create_app
from project.models.bp_catalogo import *
from project.models.bp_auth import *

app = create_app()
app.app_context().push()


def do_work():
    with app.app_context():
     
        administrador = User(username= 'mbustamc', email='mbustamc@gmail.com', is_admin=True)
        administrador.set_password('password')
        db.session.add(administrador)

        """
        productor_01 = Productor(nombre_fantasia = 'Agricola Don Pollo', razon_social ='Agricola don pollo limitada', website='http://www.donpollo.cl')
        productor_02 = Productor(nombre_fantasia = 'AEG Nutricion',razon_social = 'Alimentos el globo s.a.', website='http://www.aegnutricion.cl')
        productor_03 = Productor(nombre_fantasia = 'Aquapur', razon_social ='Aquapur limitada', website='https://aquapur.cl/')
        
        producto_01= Producto(nombre='Carne de pollo')
        producto_02= Producto(nombre='Carne de cerdo')
        producto_03= Producto(nombre='Huevos')
        producto_04= Producto(nombre='Restaurante')
        producto_05= Producto(nombre='Encurtidos')
        producto_06= Producto(nombre='Galletas')
        producto_07= Producto(nombre='Barras de cereal')
        producto_08= Producto(nombre='Alimento para animales')
        producto_09= Producto(nombre='Agua envasada')
        
        rubro_01 = Rubro(nombre='Confites, galletas y chocolates')
        rubro_02 = Rubro(nombre='Carnes')
        rubro_03 = Rubro(nombre='Lacteos, huevos y refrigerados')
        rubro_04 = Rubro(nombre = 'Bebidas y licores')
        
        productor_01.productos.append(producto_01)
        productor_01.productos.append(producto_02)
        productor_01.productos.append(producto_03)
        productor_02.productos.append(producto_06)
        productor_02.productos.append(producto_07)
        productor_02.productos.append(producto_08)
        productor_03.productos.append(producto_09)
        rubro_01.productos.append(producto_06)
        rubro_01.productos.append(producto_07)
        rubro_02.productos.append(producto_01)
        rubro_02.productos.append(producto_02)
        rubro_03.productos.append(producto_03)
        rubro_04.productos.append(producto_09)
        db.session.add_all([productor_01, productor_02, productor_03])
        db.session.add_all([producto_01, producto_02, producto_03, producto_04, producto_05, producto_06, producto_07, producto_08, producto_09])
        db.session.add_all([rubro_01, rubro_02, rubro_03, rubro_04,])
        """
        db.session.commit()	


do_work()