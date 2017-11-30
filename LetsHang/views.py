from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
#from django.views.generic import TemplateView
'''
class HomePage(TemplateView):
    template_name = 'index.html'
'''
def index(request):
    return render(request, 'LetsHang/index.html', {
    'title': 'Welcome to the Home Page Boi'
})


def login_redirect(request):
    return redirect('/accounts/login')
