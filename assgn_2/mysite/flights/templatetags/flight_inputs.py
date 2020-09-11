import datetime
from django import template
from flights.models import Airport,Customer
register = template.Library()

@register.filter(name='sql_format')
def sql_format(value):
	if not value:
		value = "NO QUERY FIRED"
	return str(value).replace("SELECT ","SELECT \n\t").replace("FROM ","\n FROM\n\t").replace("WHERE (","\n WHERE\n\t(\n\t\t ").replace("AND ","\n\t\t AND ").replace(", ",", \n\t ").replace(")","\n\t )")

@register.inclusion_tag('flights/airport_dropdown.html')
def airport_dropdown(input_label,input_name,input_value):
	return {'label':input_label,'value': input_value,'name':input_name,'airports': Airport.objects.all()}

@register.inclusion_tag('flights/customer_dropdown.html')
def customer_dropdown(customer_id):
	return {'active_customer': customer_id,'customers': Customer.objects.all()}	

@register.inclusion_tag('flights/flights_table.html')
def flights_table(flights,hide_booking=False):
	return {'flights':flights,'hide_booking': hide_booking}

