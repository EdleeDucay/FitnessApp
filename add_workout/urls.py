from django.urls import path
from . import views
# from .views import ExerciseList

urlpatterns = [
    path('', views.addWorkout, name='addWorkout'),
    # path('', ExerciseList.as_view() , name='exercises'),
    path('add_set', views.addSet, name='addSet')
]