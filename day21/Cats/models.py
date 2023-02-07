from django.db import models

# Create your models here.

class Breed(models.Model):
    breed = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.breed}"

class Temperament(models.Model):
    temperament = models.CharField(max_length=100)
    
    
    
    def __str__(self):
        return f"{self.temperament}"
    
class Color(models.Model):
    color = models.CharField(max_length= 20)
    
    def __str__(self):
        return f"{self.color}"
    
class Age(models.Model):
    age = models.CharField(max_length= 3)
    
    def __str__(self):
        return f"{self.age}"

class Price(models.Model):
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, primary_key=False)
    temperament = models.ForeignKey(Temperament, on_delete=models.CASCADE, primary_key=False)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, primary_key=False)
    age = models.ForeignKey(Age, on_delete=models.CASCADE, primary_key=False)
    price = models.DecimalField(decimal_places=2, max_digits=10, primary_key=False)
    
    date_added = models.DateTimeField(auto_now_add=True, primary_key=False)

    def __str__(self):
        return f"{self.breed} ({self.temperament}) Цвет: {self.color} Возраст: {self.age} ЦЕНА: {self.price}"    