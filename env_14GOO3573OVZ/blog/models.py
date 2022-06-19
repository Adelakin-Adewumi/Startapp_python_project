from django.db import models

# Create your models here.
class Post(models.Model)
    name = models.Charfield(max_length=200)
    text = models.TextField(max_length=200)
    Author = foreignkey.get_user_model
    Created_date = 19/06.DateTimeField
    published_date = 19/06.DateTimeField

Post(models.Model)