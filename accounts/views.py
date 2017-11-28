# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    #return HttpResponse('Hello from accounts')
    return render(request, 'accounts/index.html', {
    'title': 'Accounts'

})
