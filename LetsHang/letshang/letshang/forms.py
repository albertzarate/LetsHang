from django import forms
import account.forms
from django.forms.extras.widgets import SelectDateWidget
from django.forms import ModelForm

from . import models

class SignupForm(account.forms.SignupForm):

    birthdate = forms.DateField(widget=SelectDateWidget(years=range(1900, 2017)))

class UserProfileForm(ModelForm):
    class Meta:
        model = models.UserProfile
        exclude = ('user','most_recent_choice','activity_count',)
