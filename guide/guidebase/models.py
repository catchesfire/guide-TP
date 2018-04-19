from django.db import models

# Create your models here.


class TypeOfPlace(models.Model):
    name = models.CharField(max_length=50)


class Place(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey('TypeOfPlace', on_delete=models.CASCADE,)
    location = models.Field()
    open_hours = models.CharField(max_length=100)
    avg_visit_time = models.DurationField()
    prices = models.CharField(max_length=100)
    age_rules = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')

