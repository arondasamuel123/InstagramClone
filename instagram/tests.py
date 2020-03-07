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
        
    def test_delete_image(self):
        self.user_sam.save()
        self.profile_one.save()
        self.image_one.save_image()
        self.image_one.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)==0)
        
    def test_update_caption(self):
        self.user_sam.save()
        self.profile_one.save()
        self.image_one.save_image()
        self.image_one.get_img_id(self.image_one.id)
        self.image_one.update_cap('This is not Football')
        self.assertTrue(self.image_one.image_caption=='This is not Football')
        
class ProfileModelTestClass(TestCase):
    def setUp(self):
        self.user_john = User(username='johndoe', email='johndoe@gmail.com', password='abcdef')
        self.profile_two = Profile(profile_photo='/path/imgtwo.png', bio='This is the second bio', user=self.user_john)
        
        
    def test_save_profile(self):
        self.user_john.save()
        self.profile_two.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
    def test_delete_profile(self):
        self.user_john.save()
        self.profile_two.save_profile()
        self.profile_two.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)== 0)
        
    def test_update_bio(self):
        self.user_john.save()
        self.profile_two.save_profile()
        self.profile_two.get_prof_id(self.profile_two.id)
        self.profile_two.update_profile('This is the third bio')
        self.assertTrue(self.profile_two.bio=='This is the third bio')
        
        
        
        