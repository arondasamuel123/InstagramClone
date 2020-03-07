from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='insta/', blank=True)
    bio = models.TextField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follower_user = models.IntegerField(blank=True , null=True)
    following_user = models.IntegerField(blank=True, null=True)
    
    
class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=30)
    image_location = models.ImageField(upload_to='insta/', blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()
    @classmethod
    def get_img_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image
    
    def update_cap(self, image_caption):
        self.image_caption = image_caption
        self.save()
    
class Comment(models.Model):
    comment = models.CharField(max_length=30)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    image_id = models.ForeignKey(Image, on_delete=models.CASCADE)
    
class Like(models.Model):
    likes = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    image_id = models.ForeignKey(Image, on_delete=models.CASCADE)

class Followers(models.Model):
    f_user = models.ForeignKey(Profile, related_name='%(class)s_follower_user',on_delete=models.CASCADE)
    following_u = models.ForeignKey(Profile,related_name='%(class)s_following_user',on_delete=models.CASCADE)
    
        
    
    
