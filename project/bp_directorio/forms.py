# project/catalogo/forms.py
from flask_wtf import Form

from wtforms import  SelectField, SubmitField


from project.models import *



class ElegirRubroForm(Form):
    rubro= SelectField(u'', choices=[], coerce=int)
    
    #submit = SubmitField()
