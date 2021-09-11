from django.shortcuts import render, redirect
from .forms import EditProfileForm
from .models import User

# Create your views here.

def profile(request):
    context = {}

    #get username of logged in user from the request
    username = None
    username = request.user.username

    #get the user object from database
    user = User.objects.get(username = username)

    context['username'] = username
    context['first_name'] = user.first_name
    context['last_name'] = user.last_name
    context['weight'] = user.weight
    context['age'] = user.age
    context['height'] = user.height
    if user.weight == 0 or user.age == 0 or user.height == 0:
        context["display_message"] = True
        
    return render(request, 'profile.html', context)


def edit_profile(request):
    if (request.method == 'POST'):
    
        username = request.user.username
        user = User.objects.get(username = username)

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.weight = request.POST['weight']
        user.age = request.POST['age']
        user.height = request.POST['height']
        
        user.save()
        return redirect('/profile/')

    else:
        context ={}
        #get username of logged in user
        username = None
        # if request.user.is_authenticated():
        username = request.user.username
        print(username)
        user = User.objects.get(username = username)
        user_data = {"first_name": user.first_name, "last_name": user.last_name, "weight": user.weight, "age": user.age, "height": user.height}
        context['form']= EditProfileForm(initial=user_data)

        return render(request, 'edit_profile.html', context)
    