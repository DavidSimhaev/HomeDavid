from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    model = models.CharField(max_length=50) 
    class Meta:
        ordering = ("model",)
        verbose_name = "Категории"
        verbose_name_plural = "Категории"
         
    def __str__(self) -> str:
        return self.model
    
    
class Categorys_lighting(models.Model):
    Charging_time = models.CharField(max_length=50) 
    class Meta:
        ordering = ("Charging_time",)
        verbose_name = "Время зарядки"
        verbose_name_plural = "Время зарядки"
        
    def __str__(self) -> str:
        return self.Charging_time
    

class Camera(models.Model):
    category = models.ForeignKey(Category, related_name="Camera", on_delete=models.DO_NOTHING)
    firm = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=50)
    Matrix_format = models.CharField(max_length=30)
    Bayonet = models.CharField(max_length=30)
    lens = models.BooleanField(default=True)
    Image_Stabilizer = models.CharField(max_length=50)
    color =  models.CharField(max_length=50)
    content  = models.TextField(blank=True, max_length= 1000)
    
    image = models.ImageField(upload_to='products/%Y/%m/%d')

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    
    
    price = models.DecimalField(decimal_places= 2, max_digits =10, default=0, null= True)
    
    stock = models.PositiveBigIntegerField()
    
    def __str__(self):    
        return f"--{self.name}--, --{self.firm}--"
    
    
    def get_absolute_url(self):
        return reverse('Main:Camera_product', args=[self.id])
    
    

class lens(models.Model):
    lens =  models.ForeignKey(Category,  related_name="Lens", on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200, db_index=True)
    type = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    content = models.TextField(blank= True, max_length= 1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    stock = models.PositiveBigIntegerField()
    
    def __str__(self):
        return f"--{self.lens}--, --{self.name} --{self.price}-- "
    
    
class tripods(models.Model):
    name = models.CharField(max_length=10, db_index=True)
    content = models.TextField(blank= True, max_length= 1000)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    is_published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    stock = models.PositiveBigIntegerField()
    def __str__(self):
        return f"Tripod: {self.name}, price: {self.price}"

class lightings(models.Model):
    name = models.CharField(max_length=30, db_index=True)
    time_power = models.ForeignKey(Categorys_lighting, related_name="lighting", on_delete=models.DO_NOTHING)
    power = models.CharField(max_length=200, db_index=True)
    Charging_time = models.CharField(max_length=200, db_index=True)
    content = models.TextField(blank= True, max_length= 3000)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    stock = models.PositiveBigIntegerField()
    
    def __str__(self):
        return f"--{self.name} --{self.price}-- "
    
    
class Binoculars(models.Model):
    name = models.CharField(max_length=30, db_index=True)
    material = models.CharField(max_length=30, db_index=True)
    range = models.CharField(max_length=30, db_index=True)
    content = models.TextField(blank= True, max_length= 3000)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    stock = models.PositiveBigIntegerField()
    
    def __str__(self):
        return f"--{self.name} --{self.price}-- "