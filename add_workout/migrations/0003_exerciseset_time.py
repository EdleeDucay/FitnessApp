# Generated by Django 3.2.7 on 2021-09-11 19:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_workout', '0002_auto_20210911_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='exerciseset',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 11, 19, 24, 33, 350112)),
        ),
    ]
