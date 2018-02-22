from django.conf.urls import url
from mussels_site import views




urlpatterns = [
    # core pages
    url(r'^$', views.home, name='home'),
    url(r'contact/$', views.contact, name='contact'),
    url(r'about', views.about, name='about'),

    #team pages
    url(r'teams/green/$', views.green_team, name='green_team'),
    url(r'teams/navy/$', views.navy_team, name='navy_team'),
    url(r'teams/futures/$', views.futures_team, name='futures_team'),

    #program pages
    url(r'programs/league/$', views.league, name='league'),
    url(r'programs/pick_up/$', views.pick_up, name='pick_up'),
    url(r'programs/travel/$', views.travel, name='travel'),
    url(r'programs/skills_clinics/$', views.skills_clinics, name='skills_clinics')

]