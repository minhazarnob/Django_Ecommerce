from django.db import models
from django.contrib.auth.models import User

# Create your models here:
District_choices = (
    ('Mymensingh','Mymensingh'),
    ('Gazipur','Gazipur'),
    ('Sherpur','Sherpur'),
    ('Netrokuna','Netrokuna'),
    ('Jamalpur','Jamalpur'),
    ('Tangail','Tangail'),
    ('Shirajgonj','Shirajgonj'),
    ('Dhaka','Dhaka'),
    ('Kishoregonj','Kishoregonj'),
    ('Sunamgonj','Sunamgonj'),
    ('Rajshahi','Rajhshahi'),
    ('Pabna','Pabna'),
    ('Dinajpur','Dinajpur'),
    ('Kustia','Kustia'),
    ('Barishal','Barishal'),
    ('Narayangonj','Narayangonj'),
    ('Rangpur','Rangpur'),
    ('Chittagong','Chittagong'),
    ('Khulna','Khulna'),
    ('Jhinaidah','Jhinaidah'),
    ('Josshore','Josshore'),
    ('Joypurhat','Joypurhat'),
    ('Chandpur','Chandpur'),
    ('Nuakhali','Nuakhali'),
    ('Rangamati','Rangamati'),
    ('Madaripur','Madaripur'),
    ('Manikgonj','Manikgonj'),
    ('Sylhet','Sylhet'),
    ('Bagherhat','Bagherhat'),
    ('CoxsBazar','CoxsBazar'),
    ('Pirojpur','Pirojpur'),
    ('Laxmipur','Laxmipur'),
    ('Gaibandha','Gaibandha'),
    ('Kurigram','Kurigrham'),
    ('Kurigram','Kurigram')  
)

Category_choices = (
    ('curd','Curd'),
    ('milk','Milk'),
    ('lassi','Lassi'),
    ('milkshake','Milkshake'),
    ('paneer','Panner'),
    ('ghee','Ghee'),
    ('cheese','Cheese'),
    ('icecream','Ice-cream')
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default="")
    prod_app = models.TextField(default="")
    category = models.CharField(choices = Category_choices, max_length=10)
    product_image = models.ImageField(upload_to="product")
    
    def __str__(self):
        return self.title


class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=District_choices,max_length=100)
    
    def __str__(self):
        return self.name

    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    
STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
    ('Pending','Pending'),
)
   
class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.FloatField()
    rezorpray_order_id = models.CharField(max_length=100,blank=True,null=True)
    razorpray_payment_status = models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_id = models.CharField(max_length=100,blank=True,null=True)
    paid = models.BooleanField(default=False)
 
   
class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE,default="")
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
