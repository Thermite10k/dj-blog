from django.contrib import admin
from .models import Venue
from .models import MyClubUser
from .models import Event
# Register your models here.


#admin.site.register(Venue) or @admin... can be deleted and this line will be written after the class with nem of the class added
admin.site.register(MyClubUser)
#admin.site.register(Event)

@admin.register(Venue)
class Venue_admin(admin.ModelAdmin):
    list_display = ('Venue_name','address', 'phone') # name of rows to be shown in admin page
    ordering = ('Venue_name',) # how to sort them. ('-name',) does it in reverse
    search_fields = ('Venue_name', 'address')

@admin.register(Event)
class Event_admin(admin.ModelAdmin):
    fields = (('name', 'venue'), 'event_date', 'description', 'manager')
    list_display = ('name', 'event_date', 'venue')
    list_filter = ('event_date', 'venue')
    ordering = ('event_date',)