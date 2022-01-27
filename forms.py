from flask_wtf import FlaskForm
from wtforms import StringField,  IntegerField, SubmitField
from wtforms.validators import DataRequired, Length

class Formulario(FlaskForm):
    name = StringField('Nome completo', id = "name", validators=[DataRequired("O preenchimento desse campo é obrigatório")])
    cpf = StringField('CPF', id = "cpf",validators=[DataRequired("Este campo aceita apenas números inteiros"),Length(min=11, max=11, message="Este campo deve possuir 11 caracteres")])
    age    = StringField('Idade', id = "age",validators=[DataRequired("Este campo aceita apenas números inteiros"),Length(min=1, max=3,message="Este campo deve possuir no máximio 3 caracteres")])
    address = StringField('Endereço', id = "address",validators=[DataRequired("O preenchimento desse campo é obrigatório")])
    salvar = SubmitField('Salvar', id='salvar')