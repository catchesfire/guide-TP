from django.db import models

# Create your models here.


class TypeOfPlace(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey('TypeOfPlace', on_delete=models.CASCADE,)
    location = models.CharField(max_length=100)
    open_hours = models.CharField(max_length=100)
    avg_visit_time = models.DurationField()
    prices = models.CharField(max_length=100)
    age_rules = models.CharField(max_length=20)
    about = models.CharField(max_length=1000, default='nothing here')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name
