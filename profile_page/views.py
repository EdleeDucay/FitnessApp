from django.shortcuts import render
from .forms import EditProfileForm

# Create your views here.

def profile(request):
    # return HttpResponse("Hello, world. You're at the profile index.")
    return render(request, 'profile.html')

def edit_profile(request):
    context ={}
    context['form']= EditProfileForm()
    return render(request, 'edit_profile.html', context)