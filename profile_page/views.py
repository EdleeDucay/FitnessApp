from django.shortcuts import render
# from .models import User

# Create your views here.

def profile(request):
    # return HttpResponse("Hello, world. You're at the profile index.")
    return render(request, 'profile.html')