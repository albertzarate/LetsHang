from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
import notifications.urls
from django.contrib import admin
from . import views
from . views import SignupView

urlpatterns = [
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^admin/", include(admin.site.urls)),
    url(r'^account/signup/$', SignupView.as_view(), name="account_signup"),
    url(r"^account/", include("account.urls")),
    url(r"^selection/", include("selection.urls")),
    url(r"^notifications/", include("pinax.notifications.urls", namespace="pinax_notifications")),
    url(r"^profile/$", views.profile, name="profile"),
    #url(r'^inbox/notifications/', include(notifications.urls, namespace='notifications')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
