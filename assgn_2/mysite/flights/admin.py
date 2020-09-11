from django.contrib import admin
from flights.models import Location,Airline,Airport,Flight,Schedule,Customer,Booking

# Register your models here.
admin.site.register(Location)
admin.site.register(Airport)
admin.site.register(Airline)
admin.site.register(Flight)
admin.site.register(Schedule)
admin.site.register(Customer)
admin.site.register(Booking)