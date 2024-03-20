from django.db import models

from django.contrib.auth.models import User

from Main.models import Camera, lens, tripods, lightings, Binoculars
# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, related_name="Order", on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email =   models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=30)
    city = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    paid = models.BooleanField(default=False)
    class Meta:
        ordering = ["-created"]
        indexes = [models.Index(fields=["-created"])]
    
    def __str__(self):
        return f"Order {self.id}"
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE) # Не понял
    product = models.CharField(max_length=100) # Не понял
    price= models.DecimalField(max_digits=10, decimal_places=2)
    quantity= models.DecimalField(max_digits=10, decimal_places=2)
   
    
    def __str__(self) -> str:
        return f"{self.id}"
    
    def get_cost(self):
        return self.price * self.quantity
