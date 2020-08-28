#!/usr/bin/env python
# -*- coding: utf-8 -*-

from project import create_app
from project.models import *


app = create_app()
app.app_context().push()


def do_work():
    with app.app_context():
     
        #administrador = User(username= 'mbustamc', email='mbustamc@gmail.com', is_admin=True)
        #administrador.set_password('password')
        #db.session.add(administrador)

        productor_01 = Productor(nombre_fantasia = 'Agricola Don Pollo', 
        			razon_social ='Agricola don pollo limitada', website='http://www.donpollo.cl')
   		productor_02 = Productor(nombre_fantasia = 'AEG Nutricion',
   					razon_social = 'Alimentos el globo s.a.', website='http://www.aegnutricion.cl')
		productor_03 = Productor(nombre_fantasia = 'Aquapur',razon_social ='Aquapur limitada', website='https://aquapur.cl/')


		rubro_01= Rubro(nombre='Carne de pollo')
		rubro_02 = Rubro(nombre='Carne de cerdo')
		rubro_03 = Rubro(nombre='Huevos')
		rubro_04 = Rubro(nombre='Restaurante')
		rubro_05 = Rubro(nombre='Encurtidos')
		rubro_06 = Rubro(nombre='Galletas')
		rubro_07 = Rubro(nombre='Barras de cereal')
		rubro_08 = Rubro(nombre='Alimento para animales')
		rubro_09 = Rubro(nombre='Agua envasada')

		productor_01.rubros.append(rubro_01)
		productor_01.rubros.append(rubro_02)
		productor_01.rubros.append(rubro_03)
		productor_02.rubros.append(rubro_06)
		productor_02.rubros.append(rubro_07)
		productor_02.rubros.append(rubro_08)
		productor_03.rubros.append(rubro_09)

		session_db.add_all([productor_01, productor_02, productor_03])
		session_db.add_all([rubro_01, rubro_02, rubro_03, rubro_04, rubro_05, rubro_06, rubro_07, rubro_08, rubro_09])

        db.session.commit()	


do_work()