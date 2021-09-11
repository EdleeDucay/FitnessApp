from django import forms
from datetime import date

from django.forms import widgets
from .models import ExerciseSet

class WorkoutForm(forms.Form):
    workout_date = forms.DateTimeField()

class SetForm(forms.ModelForm):

    class Meta:
        model = ExerciseSet
        fields = ('exercise', 'weight', 'reps')


