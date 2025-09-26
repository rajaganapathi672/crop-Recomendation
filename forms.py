from flask_wtf import FlaskForm
from wtforms import FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class RecommendationForm(FlaskForm):
    nitrogen = FloatField('Nitrogen', validators=[
        DataRequired(),
        NumberRange(min=0, max=140, message="Value must be between 0-140")
    ])
    phosphorus = FloatField('Phosphorus', validators=[
        DataRequired(),
        NumberRange(min=5, max=145, message="Value must be between 5-145")
    ])
    potassium = FloatField('Potassium', validators=[
        DataRequired(),
        NumberRange(min=5, max=205, message="Value must be between 5-205")
    ])
    temperature = FloatField('Temperature (°C)', validators=[
        DataRequired(),
        NumberRange(min=8, max=44, message="Value must be between 8-44°C")
    ])
    humidity = FloatField('Humidity (%)', validators=[
        DataRequired(),
        NumberRange(min=14, max=100, message="Value must be between 14-100%")
    ])
    ph = FloatField('pH', validators=[
        DataRequired(),
        NumberRange(min=3.5, max=9.9, message="Value must be between 3.5-9.9")
    ])
    rainfall = FloatField('Rainfall (mm)', validators=[
        DataRequired(),
        NumberRange(min=20, max=300, message="Value must be between 20-300mm")
    ])
    soil_type = SelectField('Soil Type', choices=[
        ('clay', 'Clay'),
        ('sandy', 'Sandy'),
        ('loamy', 'Loamy'),
        ('black', 'Black'),
        ('red', 'Red'),
        ('laterite', 'Laterite')
    ], validators=[DataRequired()])
    submit = SubmitField('Get Recommendation')