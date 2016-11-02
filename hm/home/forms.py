from django import forms
from django.forms import ModelForm
from django.forms.widgets import SelectDateWidget
from .models import *


class SignUp(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Name' , 'class': 'form-control'}),
            'roll': forms.TextInput(attrs={'placeholder': 'Enter Roll no.', 'class': 'form-control'}),
            'dob': SelectDateWidget( years = [ i for i in range(1990 , 2016)] , empty_label="Nothing",attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'program': forms.Select(attrs={'class': 'form-control'}),
        }
