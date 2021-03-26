from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    patients = models.ManyToManyField('core.Patient', related_name='nutritionists')


class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)


class Note(models.Model):
    patient = models.ForeignKey('core.Patient', on_delete=models.CASCADE, related_name='notes')
    nutritionist = models.ForeignKey('core.User', on_delete=models.CASCADE, related_name='notes')
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Note {} on {}".format(self.patient, self.date.date().isoformat())
