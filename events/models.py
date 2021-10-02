from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Venue(models.Model):
    Venue_name = models.CharField('venue Name', max_length=60)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip Code', max_length=15, blank=True)

    phone = models.CharField('Contact Phone', max_length=20, blank=True)
    web = models.URLField('Website Address', blank=True)
    email_address = models.EmailField('Email', blank=True)
    
    
    def __str__(self): # use this model in admin page. Shows what will be retuned.
        return self.address


class   MyClubUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')
    
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Event(models.Model):
    name = models.CharField('Event name', max_length=120)
    event_date = models.DateTimeField('Event_date')
    #venue = models.CharField(max_length=120) 
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)# to connect two tables (one to many )1 event has 1 venue! and models.CASCADE is used so if we remove a venuse
    #manager = models.CharField(max_length=60)                                        # so if an event is deleted, venuse are deleted too
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL) # .SET_NULL  = if a manager delets hi accounts, the events wont be deleted
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUser, blank=True)
  
    def __str__(self): # use this model in admin page. Shows what will be retuned.
        return self.name