from django.db import models
from django.contrib.auth.models import AbstractUser

"""
    Baked into the AbstractUser:
        username
        first_name
        last_name
        password
        email
"""
class User(AbstractUser):
    pass

class Memory(models.Model):
    text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    starred = models.BooleanField(default=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
