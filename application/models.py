from django.contrib.auth.models import User
from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50)
    province = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Ciudades'

    def __str__(self):
        return self.name


class Owner_Ship(models.Model):
    description = models.CharField(max_length=200)
    capacity = models.IntegerField()
    city = models.ForeignKey(City, null=True, on_delete=models.SET_NULL)
    owner = models.ForeignKey(User, null=False, on_delete=models.SET('null'))
    image = models.CharField(null=True, blank=True, max_length=200)

    class Meta:
        verbose_name_plural = 'Propiedades'

    def __str__(self):
        return self.description


class Reservation(models.Model):
    date = models.DateTimeField()
    code = models.IntegerField()
    total = models.IntegerField()
    owner_ship = models.ForeignKey(Owner_Ship, null=False, on_delete=models.SET('null'))

    class Meta:
        verbose_name_plural = 'Reservas'

    def __str__(self):
        return self.date, self.total


class Date_Rent(models.Model):
    date = models.DateTimeField()
    owner_ship = models.ForeignKey(Owner_Ship, null=False, on_delete=models.SET('null'))
    reservation = models.ForeignKey(Reservation, null=False, on_delete=models.SET('null'))

    class Meta:
        verbose_name_plural = 'Fechas de Alquileres'

    def __str__(self):
        return self.date