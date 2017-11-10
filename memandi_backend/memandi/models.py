from django.conf import settings
from django.dispatch import receiver
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token

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

"""
    Listens for users being created and creates an 
    auth token for them when they are.
"""
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Memory(models.Model):
    text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    starred = models.BooleanField(default=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
