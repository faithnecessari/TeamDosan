from django.db import models

# Create your models here.
class Customer(models.Model):
	Fname = models.CharField(max_length=20)
	Lname = models.CharField(max_length=20)
	ContactNum = models.IntegerField()
	Street = models.CharField(max_length=20)
	City_Municipality = models.CharField(max_length=20)
	Province = models.CharField(max_length=20)
	Username = models.CharField(max_length=50)
	Password = models.CharField(max_length=20)
	repassword = models.CharField(max_length=20)

	def __str__(self):
		return self.Fname

class Admin(models.Model):
	Fname = models.CharField(max_length=20)
	Lname = models.CharField(max_length=20)
	Username = models.CharField(max_length=50)
	Password = models.CharField(max_length=20)

	def __str__(self):
		return self.Fname
	
#class Reservation(models.Model):
#	CustomerId = models.CharField(max_length=20)
#	Quantity = models.IntegerField(max_length=20)
#	Price = models.IntegerField()
#	TotalAmount = models.CharField(max_length=50)
#	PickUpDate = models.TimeField()
#	PickUpTime = models.DateField()

#class addProduct(models.Model):
    #productname = models.CharField(max_length=20)
    #productprice = models.IntegerField(max_length=20)
    #productcategory = models.CharField(max_length=20)
    
class Reservation(models.Model):
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    
