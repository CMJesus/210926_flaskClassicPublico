from flask_wtf import FlaskForm
from wtforms import DateField, StringField, FloatField, RadioField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

#Herencia desde librería, mucha funcionalidad
class MovimientoFormulario(FlaskForm):
    fecha = DateField("Fecha", validators=[DataRequired(message="Debe de informar la fecha")])
    concepto = StringField("Concepto", validators=[DataRequired(message="Debe de informar el concepto"), Length(min=10)])
    cantidad = FloatField("Cantidad", validators=[DataRequired(message="Debe de informar una cantidad"), 
                                                    NumberRange(message="Debe de informar un importe positivo", min=0.01)])
    ingreso_gasto = RadioField(validators=[DataRequired(message="Debe de informar tipo de movimiento")], 
                                            choices=[('G', 'Gasto'), ('I', 'Ingreso')])
    submit = SubmitField('Aceptar')