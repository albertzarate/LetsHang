from django.conf.urls import url, include
from django.contrib import admin
#from . import views
from django.contrib.auth import views as auth_views
from LetsHang.views import login_redirect
from LetsHang import views


'''
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/',include('accounts.urls')),
    url(r'^$', views.index, name='index'),
];
'''

urlpatterns = [
    #url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^accounts/',include('accounts.urls')),
    #url(r'^authentication/',auth_views.authentication, name='authentication'),
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('account.urls')),
]
