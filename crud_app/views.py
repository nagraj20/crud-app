from http.client import HTTPResponse
from urllib.request import Request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import users
from django.contrib import messages
from .forms import user_forms


# Create your views here.


# Create your views here.
def home(request):
    return render(request,'crud_app/home.html',)

def display_data(request):
    show_users = users.objects.all()
    return render(request,'crud_app/display_data.html',{'data': show_users})

def insert_data(request):
    if request.method == 'POST':
        if request.POST.get('first_name') and  request.POST.get('last_name') and  request.POST.get('email') and  request.POST.get('amount'):
            saverecord = users()
            saverecord.first_name = request.POST.get('first_name')
            saverecord.last_name = request.POST.get('last_name')
            saverecord.email = request.POST.get('email')
            saverecord.amount = request.POST.get('amount')
            saverecord.save()
            messages.success(request, 'The record is saved successfully!!')
            return redirect('/display')
        
    else:
        return render(request,'crud_app/insert_data.html',)





def edit_user(request,id):
    update_user = users.objects.get(id=id) 
    return render(request,'crud_app/edit_user.html',{'users':update_user})


def update(request,id):
    update_user = users.objects.get(id=id)
    form = user_forms(request.POST,instance=update_user) 
    if form.is_valid():
        form.save()
        return redirect('/display')

    return render(request,'crud_app/edit_user.html',{'users':update_user})

def del_user(request, id):
    user = users.objects.get(id = id)
    user.delete()
    return redirect('/display')
