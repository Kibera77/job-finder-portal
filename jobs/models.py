from django.db import models
from django.utils import timezone


# Create your models here.


class JobPost(models.Model):
    LOCATION = (
        ('Mombasa', 'Mombasa'),
        ('Nairobi', 'Nairobi'),
        ('Nakuru', 'Nakuru'),
        ('Embu', 'Embu'),
        ('Kisumu', 'Kisumu'),
        ('Lodwar', 'Lodwar'),
        ('Kiambu', 'Kiambu'),
        ('Vihiga', 'Vihiga'),
        ('Eldoret', 'Eldoret'),
    )

    EXPERIENCE = (
        ('1 year', '1 year'),
        ('4 years', '4 years'),
        ('7 years', '7 years'),
        ('10 years', '10 years'),
    )

    CATEGORY = (
        ('Construction', 'construction'),
        ('Teaching', 'teaching'),
        ('Farming', 'farming'),
        ('Beauty', 'beauty'),
        ('Enginering', 'enginering'),
        ('Business', 'business'),
    )

    job_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    pricing = models.FloatField()
    thumbnail = models.ImageField(null=True, blank=True, upload_to="images")
    category = models.CharField(max_length=100, null=True, blank=True, choices=CATEGORY)

    location = models.CharField(max_length=100, null=True, blank=True, choices=LOCATION)
    experience = models.CharField(max_length=50, null=True, blank=True, choices=EXPERIENCE)

    def __str__(self):
        return self.job_name


class Employees(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    qualification = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Employee'
