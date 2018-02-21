from django.db import models
import datetime



# Create your models here.

class Team(models.Model):
    team_name = models.CharField(max_length=200)
    season = models.CharField(max_length=200)
    team_description = models.CharField(max_length=1000)
    team_img = models.CharField(max_length=200)

class Owner(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    owner_img: models.CharField(max_length=200)
    owner_detail_1 = models.CharField(max_length=500)
    owner_detail_2 = models.CharField(max_length=500)
    owner_detail_3 = models.CharField(max_length=500)
    owner_detail_4 = models.CharField(max_length=500)
    owner_detail_5 = models.CharField(max_length=500)
    owner_detail_6 = models.CharField(max_length=500)

class Coach(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    coach_img = models.CharField(max_length=200)
    coach_details = models.CharField(max_length=500)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class Player(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    jersey_number = models.CharField(max_length=200)    
    position = models.CharField(max_length=200)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class Program(models.Model):
    program_title = models.CharField(max_length=200)
    cost = models.CharField(max_length=200)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    program_img = models.CharField(max_length=200)
    program_detail_1 = models.CharField(max_length=500)
    program_detail_2 = models.CharField(max_length=500)
    program_detail_3 = models.CharField(max_length=500)
    program_detail_4 = models.CharField(max_length=500)
    program_detail_5 = models.CharField(max_length=500)

class Event(models.Model):
    event_title = models.CharField(max_length=200)
    event_description = models.CharField(max_length=500)

class Location(models.Model):
    location_name = models.CharField(max_length=200)
    location_address = models.CharField(max_length=200)

class Clinic(models.Model):
    clinic_title = models.CharField(max_length=200)
    cost = models.CharField(max_length=200)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    start_time = models.DateTimeField('start time')
    end_time = models.DateTimeField('end time')
    clinic_img = models.CharField(max_length=200)
    clinic_detail_1 = models.CharField(max_length=500)
    clinic_detail_2 = models.CharField(max_length=500)
    clinic_detail_3 = models.CharField(max_length=500)
    clinic_detail_4 = models.CharField(max_length=500)
    clinic_detail_5 = models.CharField(max_length=500)

class Schedule(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    start_time = models.DateTimeField('start time')
    end_time = models.DateTimeField('end time')
    cost = models.CharField(max_length=200)

class Contact(models.Model):
    contact_type = models.CharField(max_length=200)

class Contact_Content(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    contact_url = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=200)

class Partnership(models.Model):
    partner_name = models.CharField(max_length=200)
    parnter_website = models.CharField(max_length=200)



    

    


    

    
    
    
    



