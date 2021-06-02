from django.db import models

# Create your models here.


# tweet model
class Tweet(models.Model):
    
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="images/", blank = True, null=True)
