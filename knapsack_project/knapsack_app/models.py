from django.db import models

# Create your models here.
# knapsack_app/models.py
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    weight = models.IntegerField()
    value = models.IntegerField()

    def __str__(self):
        return self.name
