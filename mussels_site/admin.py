from django.contrib import admin
from .models import Team, Owner, Coach, Player, Program, Event, Location, Clinic, Scheduled_Event, Contact, Partnership

admin.AdminSite.site_header = "Team Manager"

# #Change order of entries

# Make field sets
class TeamAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Add Team Form', {'fields': [
            'Team_Name',
            'Season',
            'Team_Description',
            'Team_Image'
        ]})
    ]

class OwnerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':[
            'First_Name',
            'Last_Name',
            'Owner_Bio_1',
            'Owner_Bio_2',
            'Owner_Bio_3',
            'Owner_Image'
        ]})
    ]

class CoachAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Add Coach Form', {'fields': [
            'Team',            
            'First_Name',
            'Last_Name',
            'Coach_Bio',
            'Coach_Image',
        ]})
    ]

class PlayerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Add Player Form', {'fields': [  
            'Team',
            'Program',
            'First_Name',
            'Last_Name',
            'Position',
            'Jersey_Number',
        ]})
    ]

class ProgramAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Add Program Form', {'fields': [
            'Program_Title',
            'Cost',
            'Start_Date',
            'End_Date',
            'Program_Image',
            'Program_Detail_1',
            'Program_Detail_2'
        ]})
    ]

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Add Event Form', {'fields': [
            'Event_Title',
            'Event_Description'
        ]})
    ]

class LocationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Add Location Form', {'fields': [
            'Location_Name',
            'Location_Address'
        ]})
    ]

class ClinicAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Add Clinic Form', {'fields': [
            'Clinic_Title',
            'Cost',
            'Start_Time',
            'End_Time',
            'Start_Date',
            'End_Date',
            'Clinic_Image',
            'Clinic_Detail_1'
        ]})
    ]

class ScheduledEventAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Add Scheduled Event Form', {'fields': [
            'Team',
            'Program',
            'Event',
            'Clinic',
            'Location',
            'Start_Time',
            'End_Time',
            'Start_Date',
            'End_Date',
            'Cost'
        ]})
    ]
class ContactAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Add Contact (Facebook, email, etc.) Form', {'fields': [
            'Contact_Type',
            'Contact_Url',
            'Contact_Number',
        ]})
    ]
class PartnershipAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Add Partner/Sponsors Form', {'fields': [
            'Partner_Name',
            'Parnter_Website'
        ]})
    ]




# Register your models here.
admin.site.register(Team, TeamAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Coach, CoachAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Clinic, ClinicAdmin)
admin.site.register(Scheduled_Event, ScheduledEventAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Partnership, PartnershipAdmin)







