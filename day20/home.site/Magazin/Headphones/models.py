from django.db import models

# Create your models here.

class bigheadphones(models.Model):
    text = models.CharField(max_length=200)
    data_added = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.text

class smoleheadphones(models.Model):
    text = models.CharField(max_length=200)
    data_added = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.text
    

class bluetoohsheadphones(models.Model):
    text = models.CharField(max_length=200)
    data_added = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.text