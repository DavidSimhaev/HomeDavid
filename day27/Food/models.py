from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User, Group
# Create your models here.


class Category(models.Model):
    categ = models.CharField(max_length=40)
    
    def __str__(self):
        return f"{self.categ}"


class Restaurant(models.Model): 
    restaurant = models.CharField(max_length=40)
    characteristic= models.TextField()
    city= models.CharField(max_length=30)
    street= models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', null=True, max_length=255)
    approved =models.DecimalField(decimal_places= 2, max_digits =10, default=0, null= True)
    
    date_added = models.DateTimeField(auto_now_add=True, primary_key=False)
    owner= models.ForeignKey(User, on_delete=models.CASCADE)
    group= models.ForeignKey(Group, on_delete=models.CASCADE, default=1) # Определение для html!
    def __repr__(self):
        return 'Image(%s, %s)' % (self.image)
    
    def __str__(self):
        return f"Ресторан: {self.restaurant}; {self.characteristic[:50]}... Город: {self.city}"     


class Menu(models.Model):
    post= models.ForeignKey(Restaurant, on_delete=models.CASCADE) 
    categ = models.ForeignKey(Category,  on_delete=models.CASCADE)
    dish = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images/', null=True, max_length=255)
    price = models.DecimalField(decimal_places= 2, max_digits =10, default=0)
    owner= models.ForeignKey(User, on_delete=models.CASCADE)
    approved =models.DecimalField(decimal_places= 2, max_digits =10, default=0, null= True)
    def __repr__(self):
        return 'Image(%s, %s)' % (self.image)

    def __str__(self):
        return f"Категория: {self.categ}; Блюдо:{self.dish}; Цена:{self.price}"     


class Comment(models.Model):  
    post = models.ForeignKey(Restaurant,  
			     on_delete=models.CASCADE,  
			     related_name='comments')  
    name = models.CharField(max_length=80)  
    email = models.EmailField()  
    body = models.TextField()  
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True)  
    active = models.BooleanField(default=True)  
      
    class Meta:  
        ordering = ('created',)  
          
    def __str__(self):  
        return 'Comment by {} on {}'.format(self.name, self.post)