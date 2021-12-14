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
    
#class Reservation(models.Model):
 
 #   date = models.CharField(max_length=20)
  #  time = models.CharField(max_length=20)
   # product = models.CharField(max_length=20)
    
class Reservation(models.Model):
	Fname = models.CharField(max_length=20)
	Lname = models.CharField(max_length=20)
	Product = models.CharField(max_length=20)
	Date = models.CharField(max_length=20)
	Time = models.CharField(max_length=20)
	
class Product(models.Model):
   # productID = models.AutoField(primary_key= True)
    shopID = models.IntegerField()
    shopName = models.CharField(max_length=20)
    productName = models.CharField(max_length=20)
    quantity = models.IntegerField()
    price = models.IntegerField()
    class Meta:
        db_table="findshopapp_product"
        
class Shops(models.Model):
    #shopID = models.AutoField(primary_key = True)
    #productName = models.CharField(max_length=20)      
    shopName = models.CharField(max_length=20)
    street = models.CharField(max_length=20)
    cityMunicipality = models.CharField(max_length=20)
    province = models.CharField(max_length=20)
    contactNumber = models.IntegerField()
    class Meta:
        db_table="findshopapp_shops"
      
class Feedback(models.Model):
	custID = models.ForeignKey(Customer, on_delete = models.CASCADE)
	shopID = models.ForeignKey(Shops, on_delete = models.CASCADE)
	email = models.CharField(max_length=50)
	subject = models.CharField(max_length=500)
	

	class meta:
		db_table = 'Feedback'