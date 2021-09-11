from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    height = models.IntegerField()
    weight = models.IntegerField()
    age = models.IntegerField()

    def __str__(self):
        return self.username