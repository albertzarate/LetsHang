from django.conf import settings
from django.db import models

class UserProfile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    birthdate = models.DateField()
    gender = models.CharField(max_length=20)
    most_recent_choice = models.IntegerField(default=0)
    activity_count = models.IntegerField(default=0)
    '''
    def __str__(self):
        return "Most Recent Choice: " + self.most_recent_choice + " - Gender: " + self.gender
'''
