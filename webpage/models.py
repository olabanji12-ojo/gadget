from django.db import models

class Hplaptop(models.Model):
    manufacturer = models.CharField(max_length=100)
    spec = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    storage = models.CharField(max_length=100)

class Dell_laptop(models.Model):
    manufacturer = models.CharField(max_length=100)
    spec = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    storage = models.CharField(max_length=100)

class Toshiba_laptop(models.Model):
    manufacturer = models.CharField(max_length=100)
    spec = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    storage = models.CharField(max_length=100)

class Techno_phone(models.Model):
    manufacturer = models.CharField(max_length=100)
    spec = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    battery_capacity = models.CharField(max_length=100)
    camera = models.CharField(max_length=100)
    storage = models.CharField(max_length=100)

class Redmi_phone(models.Model):
    manufacturer = models.CharField(max_length=100)
    spec = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    battery_capacity = models.CharField(max_length=100)
    camera = models.CharField(max_length=100)
    storage = models.CharField(max_length=100)

class Infinix_phone(models.Model):
    manufacturer = models.CharField(max_length=100)
    spec = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    battery_capacity = models.CharField(max_length=100)
    camera = models.CharField(max_length=100)
    storage = models.CharField(max_length=100)




# Create your models here