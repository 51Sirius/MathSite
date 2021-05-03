from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms.widgets import TextArea, TextInput, PasswordInput


class Answer(FlaskForm):
    answer = StringField('Ответ', validators=[DataRequired()], widget=TextInput('number'))


class Registration(FlaskForm):
    nickname = StringField('Никнэйм', validators=[DataRequired()], widget=TextInput())
    mail = StringField('Почта', validators=[DataRequired()], widget=TextInput())
    password = StringField('Пароль', validators=[DataRequired()], widget=PasswordInput())
    password_confirm = StringField('Подтверждение пароля', validators=[DataRequired(), EqualTo('password')],
                                   widget=PasswordInput())


class LoginForm(FlaskForm):
    username = StringField('Никнэйм', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
