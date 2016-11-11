from django import forms
from django.forms import ModelForm
from django.forms.widgets import SelectDateWidget
from .models import *


class SignUp(ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter password again', 'class': 'form-control'}))

    class Meta:
        model = Student
        fields = '__all__'
        error_messages = {
            }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Name' , 'class': 'form-control'}),
            'roll': forms.TextInput(attrs={'placeholder': 'Enter Roll no.', 'class': 'form-control'}),
            'dob': SelectDateWidget(
                years=[i for i in range(1990, 2016)], empty_label="Nothing",attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'program': forms.Select(attrs={'class': 'form-control'}),
            'semester': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'placeholder': 'Enter Email', 'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'placeholder': 'Enter Mobile no', 'class': 'form-control'} ),
            'father_name': forms.TextInput(attrs={'placeholder': "Enter Father's Name", 'class': 'form-control'}),
            'father_occ': forms.TextInput(attrs={'placeholder': "Enter Father's Occupation", 'class': 'form-control'}),
            'mother_name': forms.TextInput(attrs={'placeholder': "Enter  Mother's Name", 'class': 'form-control'}),
            'mother_occ': forms.TextInput(attrs={'placeholder': "Enter Mother's Occupation", 'class': 'form-control'}),
            'parent_contact': forms.TextInput(attrs={'placeholder': "Enter contact no", 'class': 'form-control'}),
            'hostel': forms.Select(attrs={ 'class': 'form-control'}),
            'room': forms.TextInput(attrs={'placeholder': 'Enter Room', 'class': 'form-control'}),
            'du': forms.TextInput(
                attrs={'placeholder': 'Enter Academic fee DU reference no', 'class': 'form-control'}),
            'mess_du': forms.TextInput(
                attrs={'placeholder': 'Enter Mess fee DU reference no', 'class': 'form-control'}),
            'local_address': forms.Textarea(
                attrs={'placeholder': 'Enter complete local address', 'class': 'form-control','rows':5}),
            'local_contact': forms.TextInput(attrs={'placeholder': "Enter contact no", 'class': 'form-control'}),
            'permanent_address': forms.Textarea(
                attrs={'placeholder': 'Enter complete address here', 'class': 'form-control', 'rows':5}),
            'town': forms.TextInput(attrs={'placeholder': 'Enter town' , 'class': 'form-control'}),
            'state': forms.TextInput(attrs={'placeholder': 'Enter State', 'class': 'form-control'}),
            'pincode': forms.TextInput(attrs={'placeholder': 'Enter pincode', 'class': 'form-control'}),
            'account': forms.TextInput(attrs={'placeholder': 'Enter Account no', 'class': 'form-control'}),
            'bank': forms.TextInput(attrs={'placeholder': 'Enter Bank name', 'class': 'form-control'}),
            'holder': forms.TextInput(attrs={'placeholder': "Enter Account holder's Name", 'class': 'form-control'}),
            'branch': forms.TextInput(attrs={'placeholder': 'Enter branch name', 'class': 'form-control'}),
            'ifsc': forms.TextInput(attrs={'placeholder': 'Enter IFSC code', 'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter password', 'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super(SignUp, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            SignUp.add_error(self,field='confirm_password',error="Password and confirm password does not match")


class LogIn(forms.Form):
    user_id = forms.CharField(max_length=8,widget=forms.TextInput(
        attrs={'placeholder': 'Enter Username', 'class': 'form-control'}))
    password = forms.CharField(max_length=20,widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter password', 'class': 'form-control'}),)
    remember_me = forms.BooleanField(required=False)

    def clean(self):
        cleaned_data = super(LogIn, self).clean()
        user_id = cleaned_data.get("user_id")
        password = cleaned_data.get("password")
        if Student.objects.filter(roll=str(user_id)).exists():
            student = Student.objects.get(roll=str(user_id))
            if password != student.password:
                LogIn.add_error(self, field='password', error="Wrong Password")
        else:
            LogIn.add_error(self, field='user_id', error="Invalid Username")


class ComplaintForm(ModelForm):
    class Meta:
        model = Complaint
        fields = '__all__'
        error_messages = {
            'complaint' : { 'min_length' : "Min length must be 50 characters" }
        }
        widgets = {
            'student': forms.TextInput(attrs={ 'class': 'form-control-static', 'readonly':True, }),
            'type': forms.Select(attrs={'class': 'form-control-static', 'readonly':True}),
            'hostel': forms.Select(attrs={'class': 'form-control'}),
            'complaint': forms.Textarea(attrs={
                'min_length':50, 'placeholder': "Enter Complaint here.....", 'class': 'form-control', 'rows':6}),
            'time' : forms.HiddenInput()
        }


class ChangePassword(forms.Form):
    user_id = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control-static', 'readonly': True, }),)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter old password', 'class': 'form-control'}), )
    new_password = forms.CharField(max_length=20, widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter New password', 'class': 'form-control'}), )
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter password again', 'class': 'form-control'}))

    def clean(self):
        cleaned_data = super(ChangePassword, self).clean()
        user_id = cleaned_data.get("user_id")
        password = cleaned_data.get("password")
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")
        if Student.objects.filter(roll=str(user_id)).exists():
            student = Student.objects.get(roll=str(user_id))
            if password != student.password:
                ChangePassword.add_error(self, field='password', error="Wrong Password")
            elif new_password != confirm_password:
                ChangePassword.add_error(
                    self,field='confirm_password',error="Password and confirm password does not match")
