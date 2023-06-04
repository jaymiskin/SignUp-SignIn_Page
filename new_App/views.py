from django.shortcuts import render, redirect
from .models import *


def index(request):
    return render(request,'index.html')

def signin_page(request):
    return render(request,'signin_page.html')


#signup_functionality
def signup(request):
    if request.method=="POST":
        try:
            user=Master.objects.get(Email=request.POST['email'])
            msg="User Alredy Exist!!!!"
            return render(request,'signup_page.html',{'msg':msg})
        except:
            password = request.POST['password']
            if password == request.POST['confirm_password']:
                master = Master.objects.create(Email = request.POST['email'],Password = password)
                print('Signup successfully.')
                return render(request,'signin_page.html')
            else:
                msg='both password should be same.'
                return render(request,'signup_page.html',{'msg':msg})
    else:
        return render(request,'signup_page.html')





# signin functionality
def signin(request):
    print(request.POST)
    try:
        master = Master.objects.get(Email = request.POST['email'])
        if master.Password == request.POST['password']:
            request.session['email'] = master.Email
            return redirect(index)

        else:
            return render(request, "signin_page.html",{'error':"Password does not match"})
    except Master.DoesNotExist as err:
        return render(request,"signin_page.html",{'error':"User does not Exists Please SignUp"})


def logout(request):
    if 'email' in request.session:
        del request.session['email']
        return redirect(signin_page)
    
    return redirect(signup)