from django.db import models

# Create your models here.


class Brand(models.Model):
    brand = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.brand}"
    
    
class Model(models.Model):
    model = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.model}"
    
class Color(models.Model):
    color = models.CharField(max_length= 15)
    
    def __str__(self):
        return f"{self.color}"
    
class Recording(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, primary_key=False)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, primary_key=False )
    color = models.ForeignKey(Color, on_delete=models.CASCADE, primary_key=False)
    
    date_added = models.DateTimeField(auto_now_add=True, primary_key=False)
    
    def __str__(self):
        return f"{self.brand} {self.model} ({self.color}) "
    