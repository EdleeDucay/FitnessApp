from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import logout, authenticate, login
# Create your views here.

def home(request):
    return render(request, 'users/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            from profile_page.models import User
            user = request.POST['username']
            user = User(username = user, first_name = "John", last_name = "Doe", weight = 0, age = 0, height = 0)
            user.save()
            return redirect('login')
            
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def loggin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print(request.user.username)
                return redirect('profile')
    else: 
        form = AuthenticationForm()
        print(request.method)
        print("what happened here")
        # return redirect('profile')

    return render(request, 'users/login.html', {'form': form})