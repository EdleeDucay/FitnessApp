from django.db import models
from django.db.models.fields import CharField
from django.utils import timezone
import datetime

# Create your models here.

class Workout(models.Model):
    date = models.DateTimeField('pub date')
    # user = models.ForeignKey(User)

Exercise_Choices = (
    ('bench', "BENCH"),
    ('squat', 'SQUAT'),
    ('deadlift', 'DEADLIFT'),
)

class ExerciseSet(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.CharField(max_length=50, choices=Exercise_Choices)
    weight = models.IntegerField()
    reps = models.IntegerField()
    time = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.exercise + ' ' + str(self.weight) + ' '  + str(self.reps)