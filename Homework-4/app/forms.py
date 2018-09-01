from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class IdForm(Form):
    user_id = StringField('user_id', validators=[DataRequired()])