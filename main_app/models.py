from django.db import models
from django import forms
from django.utils import timezone

class Finch(models.Model):
    species = models.CharField(max_length=100)
    beak_depth = models.FloatField(default=0.0)
    beak_width = models.FloatField(default=0.0)
    island = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
        return self.species

def feedings(self):
        return Feeding.objects.filter(finch=self).order_by('-date')

class Toy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    finches = models.ManyToManyField(Finch, related_name='toys')

class FinchForm(forms.ModelForm):
    class Meta:
        model = Finch
        fields = ['species', 'beak_depth', 'beak_width', 'island']

class Feeding(models.Model):
    date = models.DateField()
    quantity = models.IntegerField()
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE, related_name='feedings')

def __str__(self):
        return f"{self.date} - {self.finch.species}"

