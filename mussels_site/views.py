from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Team, Owner, Coach, Player, Program, Event, Location, Clinic, Scheduled_Event, Contact, Partnership


#base html
def base(request):
    latest_partners = Partnership.objects.all()
    return render(request,'mussels_site/partials/footer.html',{'latest_partners': latest_partners})

# core page views
def home(request):
    latest_teams = Team.objects.all()
    return render(request,'mussels_site/core/home.html', {'latest_teams':latest_teams})

def contact(request):
    return render(request,'mussels_site/core/contact.html')

def about(request):
    return render(request,'mussels_site/core/about.html')


# team page views
def green_team(request):
    return render(request,'mussels_site/teams/green.html')

def navy_team(request):
    return render(request,'mussels_site/teams/navy.html')

def futures_team(request):
    return render(request,'mussels_site/teams/futures.html')


# program and skills views
def league(request):
    return render(request, 'mussels_site/programs/league.html')

def travel(request):
    return render(request, 'mussels_site/programs/travel.html')

def pick_up(request):
    return render(request, 'mussels_site/programs/pick_up.html')

def skills_clinics(request):
    return render(request, 'mussels_site/programs/skills_clinics.html')


    