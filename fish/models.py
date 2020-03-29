from django.db import models
from django.conf import settings

# Create your models here.
class Fish(models.Model):
    LOCATIONS = [
        ('P', "Pond"),
        ('S', "Sea"),
        ('M', "River (Mouth)"),
        ('R', "River"),
        ('r', "River/Pond"),
        ('c', "River (Clifftop)"),
        ('p', "Pier"),
        ('s', "Sea (Rainy Days)"),
    ]

    SIZES = [
        ('t', "Tiny"),
        ('s', "Small"),
        ('T', "Long & Thin"),
        ('m', "Medium"),
        ('f', "Fin"),
        ('l', "Large"),
        ('L', "Very Large"),
        ('H', "Huge"),
        ("F", "Huge with Fin"),
    ]

    name = models.CharField(max_length=19, primary_key=True)
    location = models.CharField(max_length=1, choices=LOCATIONS)
    size = models.CharField(max_length=1, choices=SIZES)
    months = models.DecimalField(max_digits=4, decimal_places=0)
    times = models.DecimalField(max_digits=18, decimal_places=0)
    price = models.DecimalField(max_digits=5, decimal_places=0)


class User(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    caught = models.ManyToManyField(Fish)
    southern = models.BooleanField(default=False)
