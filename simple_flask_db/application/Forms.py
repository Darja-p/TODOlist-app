from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired,Length, ValidationError
from wtforms.fields.html5 import DateField
from .models import TODOS


class InsertingTask(FlaskForm):
    id = StringField("ID",validators=[DataRequired(),Length(min=1, max=3 )])
    description = StringField("Description",validators=[DataRequired(),Length(min=3, max=100 )])
    due_date = DateField ('Due date', format='%Y-%m-%d',validators=[DataRequired()])
    submit = SubmitField('Add')

    def validate_description (self , description) :
        task = TODOS.query.filter_by (description=description.data).first ()
        if task :
            raise ValidationError ('That task already exist')