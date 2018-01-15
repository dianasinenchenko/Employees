from django.db import models

# Create your models here.

from django.urls import reverse  # Used to generate urls by reversing the URL patterns


class Employees(models.Model):
    first_name = models.CharField(max_length=100, null=True, default=None)
    last_name = models.CharField(max_length=100, null=True, default=None)
    email = models.EmailField(null=True, default=None)


class Meta:
    ordering = ["last_name", "first_name", "email"]


def get_absolute_url(self):
    return reverse('employees-detail', args=[str(self.id)])


def __str__(self):
    return '{0}, {1}, {2}'.format(self.first_name, self.last_name, self.email)
