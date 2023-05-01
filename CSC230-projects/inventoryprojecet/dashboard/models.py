from django.db import models
from django.contrib.auth.models import User

# Create your models here.


#Creates the entry field for the product form
class Product(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.name}'

#Creates the entry fields for the order form
class Order(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.staff}-{self.name}'