from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    photo = models.ImageField(upload_to='photos', default="photos/profile-42914_960_720.png")
    gender = models.CharField(max_length=20)
    most_recent_choice = models.IntegerField(default=0)
    activity_count = models.IntegerField(default=0)

    def __self__(self):
        return self.user.get_full_name()
    def __unicode__(self):
        return self.user.get_full_name()
