from django.shortcuts import render, get_object_or_404
from .models import TeamMember

import yaml


def index(request):
    with open('/home/aahnik/Documents/django-polling_site/pollsite/home/homePage.yaml', 'r') as file:
        homePageElements = yaml.full_load(file)

    team = TeamMember.objects.order_by('title')
    context = {'hpe': homePageElements, 'team': team}
    return render(request, 'home/index.html', context)
