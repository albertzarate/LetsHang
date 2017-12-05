from django.conf import settings
from django.utils.translation import ugettext_noop as _

def create_notice_types(sender, **kwargs):
    if "pinax.notifications" in settings.INSTALLED_APPS:
        from pinax.notifications.models import NoticeType
   	    print("Creating notices for letshang")
        NoticeType.create("user_match", _("Match Received"), _("you have been matched"))
    else:
        print("Skipping creation of NoticeTypes as notification app not found")
