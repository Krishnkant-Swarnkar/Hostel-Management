from django.shortcuts import get_object_or_404, render,redirect
from .models import *
from django.http import HttpResponse
from .forms import SignUp
from django.contrib import messages
# Create your views here.
hostel_list = Hostel.objects.order_by('name')


def home(request):
    context = {'hostel_list': hostel_list}
    return render(request ,'home/index.html',context)


def hostel(request):
    context = {'hostel_list': hostel_list}
    return render(request ,'home/hostel.html',context)


def allhostel(request,hostel_id):
    cur_hostel = get_object_or_404(Hostel, pk=hostel_id)
    context = {'hostel_list': hostel_list , 'cur_hostel': cur_hostel}
    return render(request ,'home/allhostel.html',context)


def complaint(request):
    context = {'hostel_list': hostel_list}
    return render(request ,'home/complaint.html',context)


def signup(request):
    if request.method == 'POST':
        signupform = SignUp(request.POST)
        if signupform.is_valid():
            signupform.save()
            user_id = signupform.cleaned_data['roll']
            messages.add_message(request, messages.INFO, 'Sign up Successful. \\n Your USERNAME is '+str(user_id))
            return redirect(home)
    else:
        signupform = SignUp()
    context = {'hostel_list': hostel_list , 'SignUpForm' : signupform}
    return render(request ,'home/signup.html',context)
