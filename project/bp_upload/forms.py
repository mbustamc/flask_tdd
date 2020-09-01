from flask_wtf import Form
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from project import photos

	
class UploadForm(Form):
	photo = FileField(validators=[FileAllowed(photos, 'Image only!'), FileRequired('File was empty!')])
	productor = SelectField(u'', choices=[], coerce=int)