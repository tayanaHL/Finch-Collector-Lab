from django.db import models

# Create your models here.


class Finch(models.Model):
    species = models.CharField(max_length=100)
    beak_depth = models.FloatField(default=0.0)
    beak_width = models.FloatField(default=0.0)
    island = models.CharField(max_length=100)

