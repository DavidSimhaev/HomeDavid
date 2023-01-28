from django.db import models

# Create your models here.

class BMW(models.Model):
    text = models.CharField(max_length=200)
    data_added = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.text
    
class Zhiguli(models.Model):
    text = models.CharField(max_length=200)
    data_added = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.text
    

class AUDI(models.Model):
    bmw = models.ForeignKey(BMW, on_delete=models.CASCADE)
    text = models.TimeField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class meta:
        verbose_name_plural = "entries"
        def __str__(self) -> str:
            return f"{self.text[:50]}..."