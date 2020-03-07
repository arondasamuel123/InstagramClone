from django.test import TestCase
from .models import Profile, Image, Comment, Followers, Like
from django.contrib.auth.models import User

class ImageModelTestClass(TestCase):
    def setUp(self):
    
        self.user_sam = User(username='arondasamuel123', email='arondasamuel123@gmail.com', password='123456')
        self.profile_one = Profile(profile_photo='/path/image.png', bio='This is my bio', user=self.user_sam)
        self.image_one = Image(image_name='Football', image_caption='This football',image_location='/path/image.png', profile=self.profile_one)
        
        
    def test_save_image(self):
        self.user_sam.save()
        self.profile_one.save()
        self.image_one.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)> 0)