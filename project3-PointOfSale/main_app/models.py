from django.db import models
from django.urls import reverse
from .utils import GENDERS, ORDER_STATUS, PAYMENT_STATUS, PAYMENT_TYPE
from django.contrib.auth.models import User

#from enumfields import EnumField

# Create your models here.

# UserProfile - @salmanaljaziri
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDERS, default=GENDERS[0][0])
    birthdate = models.DateField()
    image = models.ImageField(upload_to='user_profile/',default="", blank=True)
    
    def get_absolute_url(self):
        return reverse('userprofiles_detail', kwargs={'pk': self.user_id})

    # Overriding    
    def __str__(self) :
        return self.phone_number
        


# ProductCategory - @yousifnooh
class ProductCategory(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=30)
    created_date=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=False)
    
    def get_absolute_url(self):
        return reverse('product_categories_detail', kwargs={'pk': self.id})

    # Overriding    
    def __str__(self) :
        return self.type


# Product - @bader-abdulla
class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=9 , decimal_places=3)
    is_taxable = models.BooleanField()
    image = models.ImageField(upload_to='product/',default="", blank=True)
    barcode = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField()
    user = models.ForeignKey (User , on_delete=models.CASCADE)
    product_category = models.ForeignKey (ProductCategory , on_delete=models.CASCADE)
    # class Meta:
    #     verbose_name_plural = "products"

    def get_absolute_url(self):
        return reverse('products_detail', kwargs={'pk': self.id})
        
    # # Overriding    
    def __str__(self) :
        return  f"{self.name} | {self.barcode}"

    

# Customer - @yousifnooh
class Customer(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=40)
    email=models.EmailField()
    phone_number=models.CharField(max_length=25)
    is_active=models.BooleanField(default=False)
    created_date=models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('customers_detail', kwargs={'pk': self.id})
    
    # # Overriding    
    def __str__(self) :
        return self.full_name
    
    

# Cart - @mahfood
class Cart(models.Model):
    cart_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_closed = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('carts_detail', kwargs={'cart_id': self.id})

    # # Overriding    
    # def __str__(self) :
    #     return self.id

    class Meta:
        ordering=['customer']



# CartItem - @mahfood
class CartItem(models.Model):
   cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
   product = models.ForeignKey(Product, on_delete=models.CASCADE,default=2)
   quantity = models.IntegerField(default=1) 

   def get_absolute_url(self):
        return reverse('cart_items_detail', kwargs={'pk': self.id})
   



# Order - @salmanaljaziri
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=1, choices=ORDER_STATUS, default=ORDER_STATUS[1][0])
    payment_type = models.CharField(max_length=1, choices=PAYMENT_TYPE, default=PAYMENT_TYPE[0][0])
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS, default=PAYMENT_STATUS[1][0])

    def get_absolute_url(self):
        return reverse('orders_detail', kwargs={'pk': self.id})

    # Overriding    
    # def __str__(self) :
    #     return self.cart.id




