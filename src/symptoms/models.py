from django.db import models
from django.urls import reverse

# Create your models here.

class Symptom(models.Model):
    symptom = models.CharField(max_length=120)

    def __str__(self):
        return self.symptom
