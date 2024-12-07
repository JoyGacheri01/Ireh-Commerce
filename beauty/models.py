from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Slider(models.Model):
    slider_title = models.CharField(max_length=100)
    slider_desc = models.CharField(max_length=100)
    slider_image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.slider_title

class About(models.Model):
    about_title = models.CharField(max_length=150)
    about_desc = models.TextField()
    about_img = models.ImageField()
    about_head = models.CharField(max_length=200)
    about_subhead = models.TextField(default="Default subtitle")

    def __str__(self):
        return self.about_title  
    
class New_Arrival(models.Model):
    CATEGORY = "new_arival"
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField()
    category = models.CharField(max_length=20, default=CATEGORY, editable=False)

    def __str__(self):
        return self.name
    
class Best_sellers(models.Model):
    CATEGORY = "best_seller"
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField()
    category = models.CharField(max_length=20, default=CATEGORY, editable=False) 

    def __str__(self):
        return self.name
    
class Discounted(models.Model):
    CATEGORY = "discounted"
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField()
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, default=CATEGORY, editable=False) 

    def __str__(self):
        return self.name

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

 

class Cleansing(models.Model):
    CATEGORY ="cleansing"
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=20, default=CATEGORY, editable=False) 

    def __str__(self):
        return self.name

class Oil(models.Model):
    CATEGORY = "oil"
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=20, default=CATEGORY, editable=False) 

    def __str__(self):
        return self.name
    
class Treatment(models.Model):
    CATEGORY = "treatment"
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=20, default=CATEGORY, editable=False) 

    def __str__(self):
        return self.name
    
class Braiding(models.Model):
    CATEGORY = "braiding"
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=20, default=CATEGORY, editable=False)
    
    def __str__(self):
        return self.name

    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products/')
    
    def __str__(self):
        return self.name

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"





