from django.db import models

# Create your models here.

class Symptom(models.Model):
    symptom         = models.CharField(max_length=120)

    # objects = SymptomManager()

    def __str__(self):
        return self.symptom
