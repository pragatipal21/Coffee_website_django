from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Service (models.Model):
    service_title=models.CharField( max_length=150)
    service_desc=models.TextField()
    service_read_link=models.CharField( max_length=150)
    service_img=models.FileField(upload_to="service/", max_length=250, null=True, default=None)



class Learn (models.Model):
    learn_heading=models.CharField(max_length=250)
    learn_title=models.CharField(max_length=250)
    learn_desc=models.TextField()
    learn_read_link=models.CharField(max_length=400)

class OurServices(models.Model):
    our_read_link=models.CharField(max_length=250)
    our_title=models.CharField(max_length=250)
    our_desc=models.TextField()
    our_img=models.FileField(upload_to="service/", max_length=500, null=True, default=None)

class pricing(models.Model):
    title=models.CharField(max_length=300)
    
    


class TableBook(models.Model):
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    date=models.CharField(max_length=150)
    time=models.CharField(max_length=150)
    person=models.CharField(max_length=150)


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    


class ContactInfo(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()


class SocialMedia(models.Model):
    url = models.URLField()
    icon_img = models.ImageField(upload_to="service/",null=True,blank=True,default=None)
    icon_class = models.CharField(max_length=50) 

class OpenHour(models.Model):
    day_range = models.CharField(max_length=50) 
    time_range = models.CharField(max_length=50)  


class Offer(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    description = models.CharField(max_length=500)




class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="service/")
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0)  # Example: 4.5 stars

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coffee_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Cart)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)



class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.message[:30]}"
