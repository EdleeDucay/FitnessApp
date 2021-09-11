from django.shortcuts import render, redirect
from .forms import EditProfileForm

# Create your views here.

def profile(request):
    #TODO grab the user info and display in the html
    return render(request, 'profile.html')


def edit_profile(request):
    if (request.method == 'POST'):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        weight = request.POST['weight']
        age = request.POST['age']
        height = request.POST['height']

        #TODO
        #UPDATE THE MODEL FIELDS OF THE USER
        return redirect('/profile/')

    else:    
        context ={}
        context['form']= EditProfileForm()

        return render(request, 'edit_profile.html', context)
    