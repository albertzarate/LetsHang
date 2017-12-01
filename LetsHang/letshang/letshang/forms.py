from django import forms
import account.forms
from django.forms.extras.widgets import SelectDateWidget

class SignupForm(account.forms.SignupForm):

    birthdate = forms.DateField(widget=SelectDateWidget(years=range(1910, 1991)))
