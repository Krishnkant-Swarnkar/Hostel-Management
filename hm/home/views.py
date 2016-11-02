from django.shortcuts import get_object_or_404, render,redirect
from .models import *
from django.http import HttpResponse
from .forms import SignUp
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
        SignUpForm = SignUp(request.POST)
        if SignUpForm.is_valid():
            redirect(home)
    else:
        SignUpForm = SignUp()
    context = {'hostel_list': hostel_list , 'SignUpForm' : SignUpForm}
    return render(request ,'home/signup.html',context)


def signedup(request):
    context = {'hostel_list': hostel_list}
    return redirect(home)