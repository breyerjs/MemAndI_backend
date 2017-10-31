from django.db import models

class Memory(models.Model):
    text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    starred = models.BooleanField(initial=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
