# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from letshang.models import UserProfile
from django.http import Http404
from letshang import apps
from django.contrib.auth.models import User
from django.apps import AppConfig
from django.conf import settings

# Create your views here.
def index(request):
    return render(request, 'selection/index.html', {})

def choice(request, selection_id):
    profiles=UserProfile.objects.all();
    for profile in profiles:
        choice=""
        name=profile.user.username
        if str(selection_id)=='1':
            choice="eat!"
            choice_id=1
            profile.most_recent_choice=1
            profile.activity_count=profile.activity_count+1
            profile.save()
        elif str(selection_id)=='2':
            choice="study!"
            choice_id=2
            profile.most_recent_choice=2
            profile.activity_count=profile.activity_count+1
            profile.save()
        elif str(selection_id)=='3':
            choice="workout!"
            choice_id=3
            profile.most_recent_choice=3
            profile.activity_count=profile.activity_count+1
            profile.save()
        else:
            raise Http404("Selection does not exist")

        return render(request, 'selection/choice.html', {'choice':choice, 'choice_id':choice_id , 'name':name,})

def match(request, selection_id):
    profiles=UserProfile.objects.all()
    for profile in profiles:
        location=""
        if str(selection_id)=='1':
            location="at the microwave next to the restrooms in the SJSU Student Union"
        elif str(selection_id)=='2':
            location="in front of the MLK Library"
        elif str(selection_id)=='3':
            location="in front of the SJSU Sport Club near the Event Center"
        else:
            raise Http404("Match Error")

    return render(request, 'selection/match.html', {'location':location})
