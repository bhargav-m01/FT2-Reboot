from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class customerform(FlaskForm):

    customercomplaint = StringField('Complaint', validators=[DataRequired()])
    submit = SubmitField("Submit",render_kw={"onclick":"addTask(event)"})