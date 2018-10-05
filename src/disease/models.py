from django.db import models

# Create your models here.

class Disease(models.Model):
    disease         = models.CharField(max_length=120)
    count           = models.IntegerField(null=True)
    # description     = models.TextField(default="Under construction")

    def __str__(self):
        return self.disease
    # def __str__(self):
        # return self.count
    # def __str__(self):
        # return self.description
