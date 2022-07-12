from django.db import models
from django.contrib.auth.models import User


# create Extends User Model

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='images')
    gender_selecation = (('Female', 'Female'),
                         ('Male', 'Male'))
    gender = models.CharField(
        choices=gender_selecation, max_length=20, default='Male')
    dob = models.DateField()

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
