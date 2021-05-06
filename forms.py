from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, NumberRange
from wtforms.widgets import TextArea, TextInput, PasswordInput, ListWidget


class Answer(FlaskForm):
    answer = StringField('Ответ', validators=[DataRequired()], widget=TextInput('number'))


class Registration(FlaskForm):
    username = StringField('Никнэйм', validators=[DataRequired()], widget=TextInput())
    email = StringField('Почта', validators=[DataRequired(), Email()], widget=TextInput())
    password = StringField('Пароль', validators=[DataRequired()], widget=PasswordInput())
    password_confirm = StringField('Подтверждение пароля', validators=[DataRequired(), EqualTo('password')],
                                   widget=PasswordInput())


class LoginForm(FlaskForm):
    username = StringField('Никнэйм', validators=[DataRequired()], widget=TextInput())
    password = PasswordField('Пароль', validators=[DataRequired()], widget=PasswordInput())
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class Settings(FlaskForm):
    username = StringField('Никнэйм', validators=[DataRequired()], widget=TextInput())
    clas = IntegerField('Класс', validators=[DataRequired(), NumberRange(min=5, max=6)], widget=TextInput('number'))
    level = IntegerField('Сложность', validators=[DataRequired(), NumberRange(min=1, max=3)], widget=TextInput('number'))
    submit = SubmitField('Изменить')