from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    role = models.CharField(max_length=10, choices=[
        ('Teacher', 'Teacher'),
        ('Student', 'Student'),])

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Mark(models.Model):
    student = models.ForeignKey(User, limit_choices_to={'role': 'student'}, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()

    class Meta:
        unique_together = ('student', 'subject')

