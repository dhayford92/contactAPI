from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    country_code = models.CharField(max_length=30)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=30)
    contact_picture = models.URLField(null=True)
    is_favorite = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name + "  " + self.last_name
