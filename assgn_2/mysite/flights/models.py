from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Location(models.Model):
	loc_id=models.CharField(max_length=5 ,primary_key=True)
	state=models.CharField(max_length=30)
	country=models.CharField(max_length=30)
	zip_code=models.CharField(max_length=10)

	def __str__(self):
		return self.state + ", " + self.country + ", " + self.zip_code

class Airline(models.Model):
	airline_id=models.CharField(max_length=10 ,primary_key=True)
	name=models.CharField(max_length=30)
	is_charter=models.BooleanField(default=False)
	upload = models.ImageField(upload_to ='static/airlines/',null=True) 

	def __str__(self):
		return "["+self.airline_id+"] " + self.name


class Flight(models.Model):
	flight_id=models.CharField(max_length=10 ,primary_key=True)
	airline=models.ForeignKey(Airline, on_delete=models.CASCADE)
	seats=models.IntegerField()

	def __str__(self):
		return "[{}] {}".format(self.airline.airline_id, 	self.flight_id)

class Airport(models.Model):
	airport_id=models.CharField(max_length=10 ,primary_key=True)
	name=models.CharField(max_length=50)
	code=models.CharField(max_length=15)
	location=models.ForeignKey(Location, on_delete=models.CASCADE)

	def __str__(self):
		return "[{}] {}".format(self.airport_id, self.name)

class Schedule(models.Model):
	schedule_id=models.CharField(max_length=10 ,primary_key=True)
	flight=models.ForeignKey(Flight,on_delete=models.CASCADE)
	src_air=models.ForeignKey(Airport,on_delete=models.CASCADE, related_name='src_air' )
	des_air=models.ForeignKey(Airport, on_delete=models.CASCADE,related_name='des_air')
	fare=models.DecimalField(max_digits=10,decimal_places=2)
	start_time=models.DateTimeField()
	end_time=models.DateTimeField()

	def __str__(self):
		return "{} {}".format(self.flight,self.start_time)

class Customer(models.Model):
	Gen = (
		('male','male'),
		('female','female'),
		)
	cust_id=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=30)
	age=models.IntegerField()
	address=models.TextField()
	location=models.ForeignKey(Location, on_delete=models.CASCADE)
	gender=models.CharField(max_length = 8, choices = Gen)
	email=models.EmailField(max_length=50)
	phone=models.CharField(max_length=20)

	def __str__(self):
		return "[{}] {}".format(self.cust_id, self.name)

class Booking(models.Model):
	schedule=models.ForeignKey(Schedule, on_delete=models.CASCADE)
	customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
	price=models.DecimalField(max_digits=10,decimal_places=2)

	def __str__(self):
		return self.schedule + " " + self.customer


