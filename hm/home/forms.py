from django import forms
from django.forms import ModelForm
from django.forms.widgets import SelectDateWidget
from .models import *


class SignUp(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'dob': SelectDateWidget( years = [ i for i in range(1990 , 2016)] , empty_label="Nothing"),
        }
