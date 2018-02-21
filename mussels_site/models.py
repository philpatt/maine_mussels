from django.db import models
import datetime



# Create your models here.

class Team(models.Model):
    Team_Name = models.CharField(max_length=200)
    Season = models.CharField(max_length=200)
    Team_Description = models.CharField(max_length=1000)
    Team_Image = models.CharField(max_length=200)

    def __str__(self):
        return self.Team_Name

class Owner(models.Model):
    First_Name = models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=200)
    Owner_Image = models.CharField(max_length=200)
    Owner_Bio_1 = models.TextField(max_length=500)
    Owner_Bio_2 = models.TextField(max_length=500)
    Owner_Bio_3 = models.TextField(max_length=500)
    
    def __str__(self):
        return (self.Lastname, self.Firstname)


class Coach(models.Model):
    First_Name = models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=200)
    Coach_Image = models.CharField(max_length=200)
    Coach_Bio = models.TextField(max_length=500)
    Team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return (self.Lastname, self.Firstname)
        
class Program(models.Model):
    Program_Title = models.CharField(max_length=200)
    Cost = models.CharField(max_length=200)
    Start_Date = models.DateField('start date')
    End_Date = models.DateField('end date')
    Program_Image = models.CharField(max_length=200)
    Program_Detail_1 = models.TextField(max_length=500)
    Program_Detail_2 = models.TextField(max_length=500)
    
    def __str__(self):
        return (self.program_title)

class Player(models.Model):
    First_Name = models.CharField(max_length=200)
    Last_Name = models.CharField(max_length=200)
    Jersey_Number = models.CharField(max_length=200)    
    Position = models.CharField(max_length=200)
    Team = models.ForeignKey(Team, on_delete=models.CASCADE)
    Program = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self):
        return (self.lastname, self.firstname)




class Event(models.Model):
    Event_Title = models.CharField(max_length=200)
    Event_Description = models.CharField(max_length=500)
    
    def __str__(self):
        return (self.Event_Title)

class Location(models.Model):
    Location_Name = models.CharField(max_length=200)
    Location_Address = models.CharField(max_length=200)
    
    def __str__(self):
        return (self.Location_Name)

class Clinic(models.Model):
    Clinic_Title = models.CharField(max_length=200)
    Cost = models.CharField(max_length=200)
    Start_Date = models.DateField('start date')
    End_Date = models.DateField('end date')
    Start_Time = models.TimeField('start time')
    End_Time = models.TimeField('end time')
    Clinic_Image = models.CharField(max_length=200)
    Clinic_Detail_1 = models.TextField(max_length=500)
    Clinic_Detail_2 = models.TextField(max_length=500)

    def __str__(self):
        return (self.Clinic_Title)


class Scheduled_Event(models.Model):
    Team = models.ForeignKey(Team, on_delete=models.CASCADE)
    Program = models.ForeignKey(Program, on_delete=models.CASCADE)
    Event = models.ForeignKey(Event, on_delete=models.CASCADE)
    Clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    Location = models.ForeignKey(Location, on_delete=models.CASCADE)
    Start_Date = models.DateField('start date')
    End_Date = models.DateField('end date')
    Start_Time = models.TimeField('start time')
    End_Time = models.TimeField('end time')
    Cost = models.CharField(max_length=200)

    def __str__(self):
        return (self.Team, self.Event)

class Contact(models.Model):
    Contact_Type = models.CharField(max_length=200)
    Contact_Url = models.CharField(max_length=200)
    Contact_Number = models.CharField(max_length=200)

    def __str__(self):
        return (self.Contact_Type)

class Partnership(models.Model):
    Partner_Name = models.CharField(max_length=200)
    Parnter_Website = models.CharField(max_length=200)

    def __str__(self):
        return (self.Partner_Name)



    

    


    

    
    
    
    



