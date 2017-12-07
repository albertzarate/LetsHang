# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#from . models import selection
from django.contrib import admin
from letshang.models import UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.
#admin.site.register(selection)
'''
class UserProfileInline(admin.StackedInline):
    model = models.UserProfile
    can_delete = False
    verbose_name_plural = 'profile'

class UserAdmin(UserAdmin):
    inlines = (UserProfileInline,)
'''
