from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")

        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exists....")
            return redirect("register")

        user = User.objects.create_user(
            username=username,
            password=password
        )
        
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        return redirect('login')
    return render( request,'register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request,username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect("tasks")
        else:
            return render(request, "login.html", {"error": "Invlid Credentials..."})
    
    
    return render(request, 'login.html')