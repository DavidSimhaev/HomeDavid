from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField

class ORDER_ID(models.Model):
    indificator = models.CharField(max_length=70)

    def __str__(self) -> str:
        return self.indificator


class Massage(models.Model):
    massage = models.CharField(max_length=50)
    class Meta:
        ordering = ['massage']
    def __str__(self):
        return self.massage



class Food(models.Model):
    food = models.CharField(max_length=50)
    class Meta:
        ordering = ['food']
    def __str__(self):
        return self.food    



class Order(models.Model):
    
    Date =  models.DateField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone =  PhoneNumberField()
    passport = models.IntegerField(validators=[MinValueValidator(0)])
    count_people = models.DecimalField(decimal_places= 0, max_digits =10, default=1 )
    count_children = models.IntegerField(blank = True, validators=[MinValueValidator(0)])
    food = models.ForeignKey(Food, related_name="Food", on_delete=models.DO_NOTHING)
    massage = models.ForeignKey(Massage,null= True, blank = True, related_name="Massage", on_delete=models.DO_NOTHING)
    boolweekends = models.BooleanField(null= True) 
    
    class Meta:
        ordering = ['food', 'massage']
    
    
    def __str__(self) -> str:
        return f'first name: {self.first_name.capitalize()} last name: {self.last_name.capitalize()}' 
    
    
    
class OrderItem(models.Model):
    
    ORDER_ID = models.ForeignKey(ORDER_ID, related_name="ORDER_ID", on_delete=models.CASCADE) 
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE) # Не понял
    product = models.CharField(max_length=100) # Не понял
    price= models.DecimalField(max_digits=10, decimal_places=2)
    quantity= models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(null= True)
    pdf_file = models.FileField(upload_to='pdfs/', blank=True, null=True)
    
    def __str__(self) -> str:
        return f"ID: {self.ORDER_ID} ORDER: {self.order}" 
    
    def get_cost(self):
        return self.price * self.quantity
    
    