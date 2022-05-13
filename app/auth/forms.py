from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import InputRequired,Email,EqualTo,length
from wtforms import ValidationError
from ..models import User

class RegistrationForm(FlaskForm):
    username = StringField(validators={InputRequired(),length(min=4,
         max=20)},render_kw={"placeholder":"username"})

    email = StringField(validators=[InputRequired(),Email()],render_kw={"placeholder":"email"})

    password = PasswordField('Password',validators = [InputRequired(),
        EqualTo('password_confirm',message = 'Passwords must match')],render_kw={"placeholder":"Password"})
    
    password_confirm = PasswordField(render_kw={'Confirm Passwords'},validators = [InputRequired()])

    submit = SubmitField("Register")

    
def validate_email(self,data_field):
    if User.query.filter_by(email =data_field.data).first():
        raise ValidationError('There is an account with that email')

def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')

class LoginForm(FlaskForm):
    email = StringField(render_kw={'Your Email Address'},validators=[InputRequired(),Email()])
    password = PasswordField(render_kw={'Password'},validators =[InputRequired()])
    remember = BooleanField(render_kw={'Remember me'})
    submit = SubmitField('Sign In')