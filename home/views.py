from django.shortcuts import render
from .models import User, ExerciseSet

# Create your views here.
def view_workouts(request):
    context = {}

    #get the exercise sets from db
    exercise_sets = ExerciseSet.objects.all()
    print(exercise_sets)
        
    return render(request, 'view_workout.html', {'exercise_sets': exercise_sets})