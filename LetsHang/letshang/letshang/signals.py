from django.db.models.signals import post_save

def create_user_profile(sender, instance, created, *args, **kwargs):
    if created:
        instance.profile = UserProfile.objects.create()
        instance.save()

post_save.connect(create_user_profile, sender=User)
