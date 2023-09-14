from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    meetups = [
        {'title': 'First Meetup', 'location': 'New York', 'slug': 'a-first-meetup'},
        {'title': 'Second Meetup', 'location': 'Paris', 'slug': 'a-second-meetup'}
    ]

    return render(request, 'meetups/index.html', {'meetups': meetups})


def meetup_details(request, meetup_slug):
    dummy_meetup = {'title': 'First Meetup', 'description': 'it is'}
    return render(request, 'meetups/meetup_details.html', {
        'meetup_title': dummy_meetup['title'],
        'meetup_description': dummy_meetup['description']
    })
