from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from django.shortcuts import render,get_object_or_404
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Airline,Schedule,Location,Airport,Customer, Booking
from collections import defaultdict

class IndexView(generic.ListView):
    template_name = 'flights/index.html'
    context_object_name = 'airlines'

    def get_queryset(self):
        return Airline.objects.all()

def SearchView(request):
    context={'form_data':{'max_price':50000}}
    if(request.POST):
        form_data = request.POST
        context['form_data'] = form_data
        query_set = Schedule.objects.filter(src_air=form_data['src_air_id'],des_air=form_data['dest_air_id'])
        if form_data['start_date']:
            query_set = query_set.filter(start_time__gte=form_data['start_date'])
        if form_data['end_date']: 
            query_set = query_set.filter(end_time__lte=form_data['end_date'])
        if form_data['max_price']: 
            query_set = query_set.filter(fare__lte=form_data['max_price'])
        context['flights'] = query_set.all()
    return render(request,'flights/search.html',context)

class AirlinesView(generic.ListView):
    template_name = 'flights/airlines.html'
    context_object_name = 'airlines'

    def get_queryset(self):
        return Airline.objects.all()

class AirportsView(generic.ListView):
    template_name = 'flights/airports.html'
    context_object_name = 'airports'

    def get_queryset(self):
        return Airport.objects.all()

class LocationsView(generic.ListView):
    template_name = 'flights/locations.html'
    context_object_name = 'locations'

    def get_queryset(self):
        for location in Location.objects.all():
            print(dir(location))
        return Location.objects.all()

def setcustomer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    request.session['customer'] = customer_id
    return JsonResponse({"error":False,"message":"Customer updated to "+str(customer)})

def BookingsView(request):
    context={}
    if(request.POST):
        customer = get_object_or_404(Customer, pk=request.session['customer'])
        schedule = get_object_or_404(Schedule, pk=request.POST['schedule_id'])
        booking = Booking(customer=customer,schedule=schedule,price=schedule.fare)
        booking.save()

    bookings = Booking.objects.all()

    customer_wise_bookings = defaultdict(lambda: [])
    for booking in bookings:
        customer_wise_bookings[booking.customer].append(booking.schedule)
    context['bookings'] = customer_wise_bookings.items()
    context['sql'] = bookings.query

    return render(request,'flights/bookings.html',context)

