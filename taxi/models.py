import os
import uuid

from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.text import slugify


def manufacturer_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)

    filename = f"{slugify(instance.name)}-{uuid.uuid4()}{extension}"

    return os.path.join("manufacturers", filename)


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)
    logo = models.ImageField(upload_to=manufacturer_image_file_path, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} {self.country}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("taxi:driver-detail", kwargs={'pk': self.pk})


def car_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)

    filename = f"{slugify(instance.model)}-{uuid.uuid4()}{extension}"

    return os.path.join("cars", filename)


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")
    image = models.ImageField(upload_to=car_image_file_path, blank=True)

    class Meta:
        ordering = ["manufacturer__name", "model"]

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse("taxi:car-detail", kwargs={'pk': self.pk})
