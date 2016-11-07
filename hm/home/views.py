import json
from django.shortcuts import get_object_or_404, render,redirect
from .models import *
from django.http import HttpResponseForbidden
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout
# Create your views here.
hostel_list = Hostel.objects.order_by('name')


def home(request):
    loginform = LogIn()
    context = {'hostel_list': hostel_list, 'LogInForm': loginform}
    return render(request ,'home/index.html',context)


def hostel(request):
    loginform = LogIn()
    context = {'hostel_list': hostel_list, 'LogInForm': loginform}
    return render(request ,'home/hostel.html',context)


def allhostel(request,hostel_id):
    cur_hostel = get_object_or_404(Hostel, pk=hostel_id)
    loginform = LogIn()
    context = {'hostel_list': hostel_list , 'cur_hostel': cur_hostel, 'LogInForm': loginform}
    return render(request ,'home/allhostel.html',context)


def complaint(request):
    loginform = LogIn()
    context = {'hostel_list': hostel_list, 'LogInForm': loginform}
    return render(request ,'home/complaint.html',context)


def signup(request):
    if request.method == 'POST':
        signupform = SignUp(request.POST)
        if signupform.is_valid():
            signupform.save()
            user_id = signupform.cleaned_data['roll']
            password = signupform.cleaned_data['password']
            email = signupform.cleaned_data['email']
            first_name = signupform.cleaned_data['name'].split(" ")[0]
            last_name = signupform.cleaned_data['name'].split(" ")[-1]
            user = User.objects.create_user(
                username=user_id,email=email,password=password,first_name=first_name,last_name=last_name)
            user.save()
            messages.add_message(request, messages.INFO, 'Sign up Successful. \\n Your USERNAME is '+str(user_id))
            return redirect(home)
    else:
        signupform = SignUp()
    loginform = LogIn()
    context = {'hostel_list': hostel_list , 'SignUpForm': signupform, 'LogInForm': loginform}
    return render(request,'home/signup.html',context)


def loging(request):
    if request.method == 'POST':
        loginform = LogIn(request.POST)
        if loginform.is_valid():
            user_id = loginform.cleaned_data['user_id']
            password = loginform.cleaned_data['password']
            user = authenticate(username=user_id, password=password)
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.INFO, 'Logged in ')
                context = {'hostel_list': hostel_list, 'LogInForm': loginform}
                return render(request, 'home/index.html', context)
    else:
        loginform = LogIn()
    context = {'hostel_list': hostel_list, 'LogInForm': loginform }
    return render(request ,'home/login.html',context)

def Logout(request):
    logout(request)
    messages.add_message(request, messages.INFO, ' Logged Out ')
    return redirect(home)