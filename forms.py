from flask_wtf import Form
from wtforms.fields import EmailField, IntegerField, StringField

STUDENTLIST = []

def add_student(student):
    STUDENTLIST.append(student)
    return STUDENTLIST

def get_list():
    return STUDENTLIST

class StudentForm(Form):
    firstname = StringField(label='first name of the student')
    lastname = StringField(label='last name of the student')
    email = EmailField(label='email')
    age = IntegerField(label='age')
    phone = StringField(label='Phone number')
