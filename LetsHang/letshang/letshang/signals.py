from django.db.models.signals import post_save

from django.db.models.signals import post_save
#from notifications.signals import notify
from letshang.models import MyModel

def create_user_profile(sender, instance, created, *args, **kwargs):
    if created:
        instance.profile = UserProfile.objects.create()
        instance.save()

post_save.connect(create_user_profile, sender=User)

'''

def my_handler(sender, instance, created, **kwargs):
    notify.send(instance, verb='was saved')

post_save.connect(my_handler, sender=MyModel)
'''
