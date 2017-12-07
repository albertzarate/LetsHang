import heapq
from django.contrib import admin
from . models import UserProfile

def heapsort(all_users_iterable): 
    h = []
    for user in all_users_iterable:
        heappush(h, user)
    return [heappop(h) for i in range(len(h))]


def most_active_member():
    if len(UserProfile.objects.all())>1: #user is admin
        all_users=UserProfile.objects.all()
        for user in all_users:
            users.append(user)
        users=heapsort(users)
        return users[len(users)-1] #returns most active member
    else:
        print 'Error: You are not an admin'

def newest_member():
    if len(UserProfile.objects.all())>1: #user is admin
        all_users=UserProfile.objects.all()
        for user in all_users:
            users.append(user)
        users=heapsort(users)
        return users[0] #returns newest member






l1=[]
l2=[]
l3=[]

print 'startup_data'
