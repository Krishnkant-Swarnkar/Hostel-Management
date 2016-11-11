import json
from django.shortcuts import get_object_or_404, render,redirect
from .models import *
from django.http import HttpResponseForbidden
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout
from django.core.mail import send_mail,mail_admins
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
    complaintform = ComplaintForm()
    context = {'hostel_list': hostel_list, 'LogInForm': loginform, 'ComplaintForm':complaintform}
    if not request.user.is_authenticated:
        messages.add_message(request, messages.INFO, 'Must be Logged in to access this page content. \\n Login First.')
        return render(request, 'home/login.html', context)
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


def submit_complaint(request):
    loginform = LogIn()
    if request.method == 'POST':
        complaintform = ComplaintForm(request.POST)
        if complaintform.is_valid():
            f=complaintform.save()
            ID = f.id
            TYPE = f.type
            COMPLAINT = f.complaint
            HOSTEL = f.hostel
            STUDENT = f.student
            TIME = f.time
            sub="Complaint"
            body='\nComplaint ID: '+str(ID)+'\nStudent Roll: '+str(STUDENT)+'\nType: '+str(TYPE)+'\nHostel: '+str(HOSTEL)+'\nComplaint : '+str(COMPLAINT)+'\nTime & Date: '+str(TIME)
            mail_admins(subject=sub, message=body, fail_silently=False)
            send_mail(subject=sub, message=body, fail_silently=False, from_email='itw2practice@gmail.com', recipient_list=['mkr8686@gmail.com'])
            messages.add_message(request, messages.INFO, 'Complaint submitted. \\n Complaint ID is '+str(ID))
            context = {'hostel_list': hostel_list, 'LogInForm': loginform, 'ComplaintForm':complaintform}
            return render(request, 'home/index.html', context)
    else:
        complaintform = ComplaintForm()
    context = {'hostel_list': hostel_list, 'LogInForm': loginform, 'ComplaintForm':complaintform }
    return render(request ,'home/complaint.html',context)


def change_password(request):
    loginform = LogIn()
    if request.method == 'POST':
        changepassword = ChangePassword(request.POST)
        if changepassword.is_valid():
            user_id = changepassword.cleaned_data['user_id']
            password = changepassword.cleaned_data['password']
            new_password = changepassword.cleaned_data["new_password"]
            confirm_password = changepassword.cleaned_data["confirm_password"]
            user = authenticate(username=user_id, password=password)
            if user is not None:
                user.set_password(new_password)
                user.save()
                student = Student.objects.get(roll__exact=user_id, password=password)
                student.password=new_password
                student.save()
                messages.add_message(request, messages.INFO, 'Password Changed')
                context = {'hostel_list': hostel_list, 'LogInForm': loginform, 'ChangePasswordForm': changepassword}
                return render(request, 'home/index.html', context)
    else:
        changepassword = ChangePassword()
    context = {'hostel_list': hostel_list, 'LogInForm': loginform, 'ChangePasswordForm': changepassword}
    return render(request, 'home/cpwd.html', context)
