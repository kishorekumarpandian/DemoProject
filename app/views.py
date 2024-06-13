from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, "app/index.html")

def Signup(request):
    if request.method == "POST":
        
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pwd1 = request.POST['pwd1']
        pwd2 = request.POST['pwd2']

        myuser = User.objects.create_user(username, email, pwd1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Successfully Created")
        return redirect('Signin')
    return render(request, "app/Signup.html")

def Signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pwd1 = request.POST['pwd1']
        user = authenticate(username=username, password=pwd1)

        if user is not None:
            fname=user.first_name
            login(request, user)
            messages.success(request,"Login Sucessfully!")
            return render(request, "app/index.html",{'fname':fname})
        else:
            messages.success(request,"Bad Credentials")
            return redirect('home')
    return render(request, "app/Signin.html")
 
def Signout(request):
    logout(request)
    messages.success(request,"Logout sucessfully!")
    return redirect('home')
    