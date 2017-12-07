import account.views
from . import forms
from . import models
from .forms import SignupForm
from .models import UserProfile
from django.shortcuts import render
from django.contrib import messages



class SignupView(account.views.SignupView):

    form_class = SignupForm

def update_profile(self, form):
    UserProfile.objects.create(
        user=self.created_user,
        birthdate=form.cleaned_data('birthdate'),
    )

    def after_signup(self, form):
        self.update_profile(form)
        super(SignupView, self).after_signup(form)

def profile(request):
    try:
        profile = request.user.userprofile
    except models.UserProfile.DoesNotExist:
        profile = None
    if request.method == 'POST':
        form = forms.UserProfileForm(request.POST, request.FILES,
                                     instance=profile)
        if form.is_valid():
            if profile:
                form.save()
            else:
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
    form = forms.UserProfileForm(instance=profile)
    context = dict(form=form)
    return render(request, 'letshang/profile.html', context)
