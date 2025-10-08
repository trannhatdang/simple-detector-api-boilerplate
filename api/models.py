from django.db import models
from . import run_model

# Create your models here. Deng: Models are just classes, used to store shit

class BasicText(models.Model):
    text = models.TextField()
    score = models.FloatField()

    def __str__(self):
        return self.text
