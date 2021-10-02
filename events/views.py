from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, Venue # Import the db
from .forms import VenueForm, EventForm
from django.http import HttpResponseRedirect, HttpResponse
import csv
# Import pagination stuff
from django.core.paginator import Paginator

def venue_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=venues.csv'
    
    # csv writer
    writer = csv.writer(response)
    # designate database
    venues = Venue.objects.all()
   # add column headings
    writer.writerow(['Venue name', 'Address', 'Phone', 'Zip code', 'Web', 'email'])
    for venue in venues:    
        writer.writerow([venue.Venue_name, venue.address, venue.phone, venue.zip_code, venue.web, venue.email_address])
        
    return response

# text file venue list

def venue_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=venues.txt'
    
    # designate database
    
    venues = Venue.objects.all()
    
    # loop through the database
    lines = []
    for venue in venues:
        lines.append(f'{venue.Venue_name}\n{venue.address}\n{venue.phone}\n{venue.zip_code}\n{venue.web}\n{venue.email_address}\n\n\n')
    #lines = ["This is line 1\n",
    #    "this is line2\n",
    #    "this is line3\n"]
    # Write t TextFile
    response.writelines(lines)
    return response
def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    
    return redirect('list-venues')


def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    
    return redirect('list_events')


def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('list_events')
    return render(request, 'events/update_event.html', {
    'event': event,
    'form': form
    })    
    
    
def add_event(request):
    submitted = False
    if request.method == "POST": # clicking the vutton   =  POST
        form = EventForm(request.POST) # if POSt than update the model
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:    
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_event.html', {
    'form': form,
    'submitted': submitted})



def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue) #instance already fills it!
    if form.is_valid():
        form.save()
        return redirect('list-venues')   
    return render(request, 'events/update_venue.html',{
    'venue': venue,
    'form': form
    })



def search_venues(request):

    if request.method == "POST": 
        searched = request.POST['searched'] 
        venues = Venue.objects.filter(Venue_name__contains=searched)
        
        return render(request, 'events/search_venues.html', {
        'searched': searched,
        'venues': venues})
    else:
        return render(request, 'events/search_venues.html', {
        
        })
    


def show_venue(request, venue_id): # venue_id was passed in urls.py!
    venue = Venue.objects.get(pk=venue_id) # primary key
    return render(request, 'events/show_venue.html', {
    'venue': venue
    })
    
    
def list_venues(request):
    #venue_list = Venue.objects.all().order_by('Venue_name') # colect all venues for ordering randomly everytime '?' can be used
    venue_list = Venue.objects.all()
    
    # Setup Pagination
    p = Paginator(Venue.objects.all(), 2) # 2nd arg is how many/page
    page = request.GET.get('page')
    venues = p.get_page(page)
    nums = "a" * venues.paginator.num_pages
    
    return render(request, 'events/venue.html', {
    'venue_list': venue_list,
    'venues': venues,
    'nums': nums,
    })



def add_venue(request):
    submitted = False
    if request.method == "POST": # clicking the vutton   =  POST
        form = VenueForm(request.POST) # if POSt than update the model
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:    
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_venue.html', {
    'form': form,
    'submitted': submitted})



def all_events(request): 


    event_list = Event.objects.all().order_by('name') # colect all events .orde_by(name of row) add ('-row') to do it opposite
    
    return render(request, 'events/event_list.html', {
    'event_list': event_list,
    })
    

def home(request, year=int(datetime.now().year), month=datetime.now().strftime('%B')):


    name = 'Ali'
    # convert month from name to numver
    month = month.capitalize() 
    month_number  = list(calendar.month_name).index(month) # or .title() to upper everything
    month_number  = int(list(calendar.month_name).index(month))
    
    # create Calendar
    cal = HTMLCalendar().formatmonth(
    year,
    month_number)
    # get current year
    now = datetime.now()
    current_year = now.year
    # get time
    time = now.strftime('%I:%M %p')
    
    return render(request, 'events/home.html', {
    "name": name,
    "year": year,
    "month": month,
    "month_number": month_number,
    "cal": cal,
    "current_year":current_year,
    "time": time,
    })

 