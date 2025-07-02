from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Teacher(AbstractUser):
    # You can add extra fields here if needed, for example:
    # department = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

    def __str__(self):
        return self.username

    # pass  # You can customize later if needed


class Student(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    score = models.IntegerField()

    def __str__(self):
        return self.name
