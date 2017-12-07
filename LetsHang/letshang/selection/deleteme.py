# -*- coding: utf-8 -*-
'''
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
    profiles=UserProfile.objects.all()
    for profile in profiles:
        choice=""
        location=""
        name=profile.user.username
        #other_user=User.objects.exclude(id=request.user.id).filter(userprofile__nost_recent_choice=1).order_by('is_active')[0]
        if str(selection_id)=='1':
            choice="eat!"
            choice_id=1
            profile.most_recent_choice=1
            profile.activity_count=profile.activity_count+1
            profile.save()
            other_user=UserProfile.objects.exclude(user_id=profile.user_id).filter(most_recent_choice=1).get()
        elif str(selection_id)=='2':
            choice="study!"
            choice_id=2
            profile.most_recent_choice=2
            profile.activity_count=profile.activity_count+1
            profile.save()
            other_user=UserProfile.objects.exclude(user_id=profile.user_id).filter(most_recent_choice=2).get()
        elif str(selection_id)=='3':
            choice="workout!"
            choice_id=3
            profile.most_recent_choice=3
            profile.activity_count=profile.activity_count+1
            profile.save()
            other_user=UserProfile.objects.exclude(user_id=profile.user_id).filter(most_recent_choice=3).get()
        else:
            raise Http404("Selection does not exist")
        if other_user:
            if str(selection_id)=='1':
                location="at the microwave next to the restrooms in the SJSU Student Union"
            elif str(selection_id)=='2':
                location="in front of the MLK Library"
            elif str(selection_id)=='3':
                location="in front of the SJSU Sport Club near the Event Center"
            return render(request, 'selection/match.html', {'choice':choice, 'choice_id':choice_id , 'name':name, 'other_user':other_user,"location":location})
        else:
            return render(request, 'selection/choice.html', {'choice':choice, 'choice_id':choice_id , 'name':name})
'''
