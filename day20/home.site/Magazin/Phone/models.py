from django.db import models

# Create your models here.

class Android(models.Model):
    text = models.CharField(max_length= 200)
    data_added = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.text
    
class Apple(models.Model):
    text = models.CharField(max_length= 200)
    data_added = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.text
    
class Xiaomi(models.Model):
    text = models.CharField(max_length= 200)
    data_added = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.text