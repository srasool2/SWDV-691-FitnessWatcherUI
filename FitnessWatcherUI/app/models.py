from django.db import models

# Create your models here.
import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    '''
    Django model to store the profile details of the user.
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    fat_percentage = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    target = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

    class Meta:
        managed = True
        db_table = 'Profile'

class WorkoutPlan(models.Model):
    workout_id = models.AutoField(primary_key=True)
    workout_name = models.CharField(max_length=20)
    workout_duration = models.IntegerField(default=45)

    def __str__(self):
        return self.workout_name

    class Meta:
        managed=True
        db_table = 'workout_plan'

class ExerciseTrack(models.Model):
    exercise_id = models.AutoField(primary_key=True)
    exercise_name = models.CharField(max_length=50)
    calorie_burnt_per_set = models.IntegerField(default=50)

    def __str__(self):
        return self.exercise_name

    class Meta:
        managed=True
        db_table = 'exercise_track'

class WorkoutPlanDetails(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    exercise_id = models.ForeignKey(ExerciseTrack, on_delete=models.CASCADE)
    num_sets = models.IntegerField(default=3)

    def __str__(self):
        return self.workout_plan.workout_name + '-'+self.exercise_id.exercise_name

    class Meta:
        managed=True
        db_table = 'workout_plan_details'    

class Blogs(models.Model):
    blog_id = models.AutoField(primary_key=True)
    blog_link = models.URLField(max_length=250)
    blog_summary = models.CharField(max_length=400)
    blog_title = models.CharField(max_length=100)

    def __str__(self):
        return self.blog_title

    class Meta:
        managed=True
        db_table='blogs'