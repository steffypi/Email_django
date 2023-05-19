from django.db import models

# Create your models here.
class application(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    place=models.TextField(max_length=20)
    age=models.IntegerField()
    email_field = models.EmailField(max_length=254)
    