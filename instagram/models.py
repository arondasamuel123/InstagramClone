from django.db import models
from django.contrib.auth.models import User

class Profile(User):
    profile_photo = models.ImageField(upload_to='insta/', blanl=True)
    bio = models.TextField(max_length=30)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    follower_user = models.IntegerField()
    following_user = models.IntegerField()
    
    
class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=30)
    image_location = models.ImageField(upload_to='insta/', blank=True)
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
class Comment(models.Model):
    comment = models.CharField(max_length=30)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    image_id = models.ForeignKey(Image, on_delete=models.CASCADE)
    
class Like(models.Model):
    likes = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    image_id = models.ForeignKey(Image, on_delete=models.CASCADE)

class Followers(models.Model):
    follower_user = models.ForeignKey(User, on_delete=models.CASCADE)
    following_user = models.ForeignKey(User, on_delete=models.CASCADE)
    
        
    
    
