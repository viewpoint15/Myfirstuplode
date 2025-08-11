from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class userdata(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    door_no = models.IntegerField(max_length = 50)
    street = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    pin_code = models.IntegerField()
    profile_pic = models.ImageField(upload_to='media/userimg', null=True, blank=True)
