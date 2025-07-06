from django.db import models
import datetime

# Create your models here.

# Categories of Products
class categories(models.Model):
    Category = models.CharField( max_length=50)

    def __str__(self):
        return self.Category
    


# Customer
class customer(models.Model): 

    first_name =models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
#product
class product(models.Model):
    name = models.CharField( max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2,  default = 0)
    categories = models.ForeignKey(categories,on_delete=models.CASCADE, default = 1)
    description = models.CharField( max_length=240)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)


    def __str__(self):
        return self.name
    


# order
class order(models.Model):

    product = models.ForeignKey("product",on_delete=models.CASCADE)
    customer = models.ForeignKey(customer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(default = '',blank =True, max_length=100)
    phone = models.CharField(blank = True, max_length=50)
    date = models.DateField(default = datetime.datetime.today)
    status = models.BooleanField(default = False)

    def __str__(self):
        return str(self.product)
    