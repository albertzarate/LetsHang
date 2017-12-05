import account.views

from .forms import SignupForm
from .models import UserProfile

class SignupView(account.views.SignupView):

    form_class = SignupForm

def update_profile(self, form):
    UserProfile.objects.create(
        user=self.created_user,
        birthdate=form.cleaned_data('birthdate'),
        #most_recent_choice=form.IntegerField()
    )

    def after_signup(self, form):
        self.update_profile(form)
        super(SignupView, self).after_signup(form)
