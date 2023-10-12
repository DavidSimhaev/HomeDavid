from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
# Create your models here.
from django.contrib.auth.models import User
class Category(models.Model):
    model = models.CharField(max_length=50) 
    class Meta:
        ordering = ("model",)
        verbose_name = "Категории"
        verbose_name_plural = "Категории"
         
    def __str__(self) -> str:
        return self.model
    
    def klass( self ):
        return self.__class__.__name__
    
class Color(models.Model):
    color =  models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.color


class Categorys_lighting(models.Model):
    Charging_time = models.CharField(max_length=50) 
    class Meta:
        ordering = ("Charging_time",)
        verbose_name = "Время зарядки"
        verbose_name_plural = "Время зарядки"
        
    def __str__(self) -> str:
        return self.Charging_time
    def klass( self ):
        return self.__class__.__name__
    
    


class Camera(models.Model):
    category = models.ForeignKey(Category, related_name="Camera", on_delete=models.DO_NOTHING)
    firm = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=50)
    Matrix_format = models.CharField(max_length=30)
    Bayonet = models.CharField(max_length=30)
    lens = models.BooleanField(default=True)
    Image_Stabilizer = models.CharField(max_length=50)
    color =  models.ForeignKey(Color, related_name="Camera", on_delete=models.DO_NOTHING)
    
    hand = models.BooleanField(default=False)
    content  = models.TextField(blank=True, max_length= 1000)
    image = models.ImageField(upload_to='products/%Y/%m/%d')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    price = models.DecimalField(decimal_places= 2, max_digits =10, default=0, null= True)
    stock = models.PositiveBigIntegerField()
    
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    
    def __str__(self):    
        return f"OBJ: {self.id}: {self.firm} NAME: {self.name} COLOR: {self.color}"
    
    def klass( self ):
        return self.__class__.__name__
    
    def get_absolute_url(self):
        return reverse('Main:Camers_product', args=[self.id, self.klass()]  )



class IMG_FILES(models.Model):
    post = models.ForeignKey(Camera, default=None, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to="post_images/",
                              verbose_name='Image')
    def __str__(self):
        return f"--OBJECT: {self.post}--"
    






  
    

class lens(models.Model):
    lens =  models.ForeignKey(Camera,  related_name="Lens", on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200, db_index=True)
    type = models.CharField(max_length=200, db_index=True)
    color =  models.ForeignKey(Color, related_name="lens", on_delete=models.DO_NOTHING)

    hand = models.BooleanField(default=False)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    content = models.TextField(blank= True, max_length= 1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    stock = models.PositiveBigIntegerField()
    
    def __str__(self):
        return f"--{self.lens}--, --{self.name} --{self.price}-- "
    def klass( self ):
        return self.__class__.__name__
    def get_absolute_url(self):
        return reverse('Main:Lens_product', args=[self.id, self.klass()]  )
    

class IMG_FILES_LENS(models.Model):
    post = models.ForeignKey(lens, default=None, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to="post_images/",
                              verbose_name='Image')
    def __str__(self):
        return f"--OBJECT: {self.post}--"
    


    
    
    
    
class tripods(models.Model):
    name = models.CharField(max_length=10, db_index=True)
    content = models.TextField(blank= True, max_length= 1000)
    color =  models.ForeignKey(Color, related_name="tripods", on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    is_published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    stock = models.PositiveBigIntegerField()
    def __str__(self):
        return f"Tripod: {self.name}, price: {self.price}"
    def klass( self ):
        return self.__class__.__name__
    def get_absolute_url(self):
        return reverse('Main:Tripods_product', args=[self.id, self.klass()]  )


class IMG_FILES_TRIPODS(models.Model):
    post = models.ForeignKey(tripods, default=None, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to="post_images/",
                              verbose_name='Image')
    def __str__(self):
        return f"--OBJECT: {self.post}--"
    


class lightings(models.Model):
    name = models.CharField(max_length=30, db_index=True)
    time_power = models.ForeignKey(Categorys_lighting, related_name="lighting", on_delete=models.DO_NOTHING)
    power = models.CharField(max_length=200, db_index=True)
    Charging_time = models.CharField(max_length=200, db_index=True)
    color =  models.ForeignKey(Color, related_name="lightings", on_delete=models.DO_NOTHING)
    content = models.TextField(blank= True, max_length= 3000)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    stock = models.PositiveBigIntegerField()
    
    def __str__(self):
        return f"--{self.name} --{self.price}-- "
    def klass( self ):
        return self.__class__.__name__
    
    def get_absolute_url(self):
        return reverse('Main:Lightings_product', args=[self.id, self.klass()]  )
class IMG_FILES_LIGHTS(models.Model):
    post = models.ForeignKey(lightings, default=None, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to="post_images/",
                              verbose_name='Image')
    def __str__(self):
        return f"--OBJECT: {self.post}--"
      
    
    
class Binoculars(models.Model):
    name = models.CharField(max_length=30, db_index=True)
    material = models.CharField(max_length=30, db_index=True)
    range = models.CharField(max_length=30, db_index=True)
    color =  models.ForeignKey(Color, related_name="Binoculars", on_delete=models.DO_NOTHING)
    
    content = models.TextField(blank= True, max_length= 3000)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    stock = models.PositiveBigIntegerField()
    
    def __str__(self):
        return f"--{self.name} --{self.price}-- "
    
    def klass( self ):
        return self.__class__.__name__
    
    
    def get_absolute_url(self):
        return reverse('Main:binoculars_product', args=[self.id, self.klass()]  )
    
class IMG_FILES_BINOCULARS(models.Model):
    post = models.ForeignKey(Binoculars, default=None, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to="post_images/",
                              verbose_name='Image')
    def __str__(self):
        return f"--OBJECT: {self.post}--"
      
    
class account_data(models.Model):
    username = models.CharField(max_length=30)
    key = models.CharField(max_length=30)
    value = models.CharField(max_length=30, null=True, blank=True)
    class Meta:
        unique_together = ("username", "key")