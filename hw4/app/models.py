from django.db import models

class Car(models.Model):
    cars_brand = models.CharField(max_length=20)
    release_date = models.IntegerField(default=None)
    cars_colour = models.CharField(max_length=20)
    cars_probeg = models.IntegerField(default=None)
    cars_price = models.IntegerField(default=None)

    def __str__(self):
        return f'{self.cars_brand} - {self.cars_probeg} - {self.cars_price} - {self.release_date}'
