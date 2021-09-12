from add_workout.models import ExerciseSet
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import WorkoutForm, SetForm
from django.utils import timezone
import datetime
from django.views.generic.list import ListView

# Create your views here.
def addSet(request):
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = SetForm(request.POST)
        
        # Check if data is valid
        if form.is_valid():
            # process the data
            form.save()
            return HttpResponse('WORKS')
    else:
        form = SetForm()

    return render(request, 'add_set.html', {'form': form})

exercise_sets = []

def addWorkout(request):
    
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = SetForm(request.POST, initial={'time': datetime.datetime.now()})
        
        # Check if data is valid and handle accordingly
        if form.is_valid() and 'addSet' in request.POST:
            # Adding set to the workout
            exercise_sets.append(form)
            print("COUNT: " + str(len(exercise_sets)))
        
        elif form.is_valid() and 'addWorkout' in request.POST:
            # Saving list of sets to the database
            for exercise in exercise_sets:
                exercise.save()
            exercise_sets.clear()

            # Redirect to homepage
            return HttpResponse('done')

        elif 'reset' in request.POST:
            exercise_sets.clear()
            form = SetForm()


    else:
        exercise_sets.clear()
        form = SetForm()

    return render(request, 'add_workout.html', {'form': form, 'exercise_sets': exercise_sets})
