from django.urls import path

from . import views

app_name = 'flights'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('search', views.SearchView, name='search'),
    path('airlines', views.AirlinesView.as_view(), name='airlines'),
    path('airports', views.AirportsView.as_view(), name='airports'),
    path('locations', views.LocationsView.as_view(), name='locations'),
    path('setcustomer/<int:customer_id>', views.setcustomer, name='setcustomer'),
    path('bookings', views.BookingsView, name='bookticket')
]