from django.db import models


class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=30)
    image_location = models.ImageField(upload_to='insta/', blank=True)
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    
