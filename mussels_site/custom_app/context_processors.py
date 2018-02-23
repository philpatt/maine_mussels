from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Team, Owner, Coach, Player, Program, Event, Location, Clinic, Scheduled_Event, Contact, Partnership

def partnership_processor(request):
    partners = Partnership.objects.all()
    return {'partners': partners}