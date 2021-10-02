from django import forms
from django.forms import ModelForm
from .models import Venue,Event


# Create a venue forma


class EventForm(ModelForm):
    class Meta:
        model = Event # from models.py
        #fields = '__all__'  
        fields = ('name', 'event_date', 'venue', 'manager', 'attendees', 'description')
        labels = {
            'name': '', # for styling
            'event_date': 'YYYY-MM-DD HH:MM:SS',
            #'zipcode': '',
            'venue': 'Venue',
            'manager': 'Manager',
            'attendees': 'Attendees',
            'description': ''
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event name'}), # for styling
            'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Date'}),
            'venue': forms.Select(attrs={'class':'form-select', 'placeholder':'Venue'}),
            'manager': forms.Select(attrs={'class':'form-select', 'placeholder':'Manager'}),
            'attendees': forms.SelectMultiple(attrs={'class':'form-select', 'placeholder':'Attendees'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'})
            
        }


class VenueForm(ModelForm):
    class Meta:
        model = Venue # from models.py
        #fields = '__all__'  
        fields = ('Venue_name', 'address', 'zip_code', 'phone', 'web', 'email_address')
        labels = {
            'Venue_name': '', # for styling
            'address': '',
            #'zipcode': '',
            'phone': '',
            'web': '',
            'email_address': '',
            'zip_code': ''
        }
        widgets = {
            'Venue_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Venue name'}), # for styling
            'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
            #'zipcode': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip code'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}),
            'web': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Web'}),
            'email_address': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email Adderss'}),
            'zip_code': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip code'})
            
        }