from django.db import models
from django.urls import reverse

# Create your models here.

class Bikes(models.Model):
    name=models.CharField(max_length=30)
    engine=models.CharField(max_length=40)
    milage=models.IntegerField()
    price=models.FloatField()

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk':self.pk})