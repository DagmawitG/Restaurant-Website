from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Hero(models.Model):
    restaurantName = models.CharField(max_length=100, verbose_name="Restaurant name", default="El Deliciós d'Etiopia")
    restaurantMotto = models.TextField(verbose_name="Restaurant Motto", default='Fresh and Delicious Ethiopian Food just for you!')
    def __str__(self):
        return self.restaurantName

class About(models.Model):
    aboutTitle = models.CharField(max_length=100, verbose_name="About Us Title", default='About Us')
    aboutPar1 = models.TextField(verbose_name="About us content 1", default='')
    aboutPar2 = models.TextField(verbose_name="About us content 2", default='')
    aboutPar3 = models.TextField(verbose_name="About us content 3", default='')
    def __str__(self):
        return self.aboutTitle

class WhyUs(models.Model):
    whyUsTitle = models.CharField(max_length=100, verbose_name="Why Us title", default='Why choose our restaurant')
    whyUs1 = models.CharField(max_length=100, verbose_name="Title 1", default='')
    whyUsDesc1 = models.TextField(verbose_name="Content 1", default='')
    whyUs2 = models.CharField(max_length=100, verbose_name="Title 2", default='')
    whyUsDesc2 = models.TextField(verbose_name="Content 2", default='')
    whyUs3 = models.CharField(max_length=100, verbose_name="Title 3", default='')
    whyUsDesc3 = models.TextField(verbose_name="Content 3", default='')
    def __str__(self):
        return self.whyUsTitle

class Footer(models.Model):
    footerTitle = models.CharField(max_length=100, verbose_name="Restaurant name", default="El Deliciós d'Etiopia")
    footerBody = models.CharField(max_length=200, verbose_name="Restaurant Motto", default='Fresh and Delicious Ethiopian Food just for you!')
    year = models.TextField(max_length=100, default='2021', verbose_name="Year")
    copyrightText = models.TextField(max_length=100, verbose_name="Copyright text")
    def __str__(self):
        return self.footerTitle

class Link(models.Model):
    twitterLink = models.TextField(max_length=100, verbose_name="Twitter Link")
    facebookLink = models.TextField(max_length=100, verbose_name="Facebook Link")
    instagramLink = models.TextField(max_length=100, verbose_name="Instagram Link")
    linkedinLink = models.TextField(max_length=100, verbose_name="LinkedIn Link")
    whatsappLink = models.TextField(max_length=100, verbose_name="WhatsApp Link")
    telegramLink = models.TextField(max_length=100, verbose_name="Telegram Link")



class Location(models.Model):
    avenue = models.CharField(max_length=200, verbose_name="Avenue")
    city = models.CharField(max_length=100, verbose_name="City")
    country = models.CharField(max_length=100, verbose_name="Country")
    def __str__(self):
        return self.avenue +" " + self.city +", "+ self.country

class OpeningHour(models.Model):
    weekdays_startTime  = models.CharField(max_length=100, verbose_name="Weekdays Opening time")
    weekdays_endTime = models.CharField(max_length=100, verbose_name="Weekdays Closing time")
    weekends_startTime  = models.CharField(max_length=100, verbose_name="Weekends Opening time")
    weekends_endTime = models.CharField(max_length=100, verbose_name="Weekends Closing time")

    def __str__(self):
        return self.weekdays_startTime +" " + self.weekdays_endTime + ", " + self.weekends_startTime+ " " + self.weekends_endTime

class Email(models.Model):
    email_address  = models.TextField(max_length=100, verbose_name="Email address")
    def __str__(self):
        return self.email_address

class Call(models.Model):
    phone_number  = models.TextField(max_length=100, verbose_name="Phone number")
    def __str__(self):
        return self.phone_number

class StarterMenu(models.Model):
    starterOption = models.CharField(max_length=100, default="Starter", editable=False)
    starterContent = models.CharField(max_length=100, verbose_name="Starter name")
    starterDesc = models.TextField(verbose_name="Starter content")
    starterPrice = models.CharField(max_length=100, verbose_name="Price")
    def __str__(self):
        return self.starterContent
    
class MainMenu(models.Model):
    mainOption = models.CharField(max_length=100, default="Main", editable=False)
    mainContent = models.CharField(max_length=100, verbose_name="Food name")
    mainDesc = models.TextField(verbose_name="Food content")
    mainPrice = models.CharField(max_length=100, verbose_name="Price")
    def __str__(self):
        return self.mainContent
    
class DessertMenu(models.Model):
    dessertOption = models.CharField(max_length=100, default="Dessert", editable=False)
    dessertContent = models.CharField(max_length=100, verbose_name="Dessert name")
    dessertDesc = models.TextField(verbose_name="Dessert content")
    dessertPrice = models.CharField(max_length=100, verbose_name="Price")


    def __str__(self):
        return self.dessertContent
    
class DrinksMenu(models.Model):
    drinksOption = models.CharField(max_length=100, default="Drink", editable=False)
    drinksContent = models.CharField(max_length=100, verbose_name="Drink name")
    drinksDesc = models.TextField(verbose_name="Drink content")
    drinksPrice = models.CharField(max_length=100, verbose_name="Price")
    def __str__(self):
        return self.drinksContent
class Rating(models.Model):
    value  = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ], verbose_name="Rating")
    def __str__(self):
        return str(self.value)

class Testimonial(models.Model):
    testimonial_subject  = models.TextField(max_length=100, verbose_name="Name")
    rating  = models.ForeignKey(Rating, on_delete=models.CASCADE)
    content  = models.TextField(verbose_name="Testimonial Content")
    def __str__(self):
        return self.testimonial_subject
        
# eventImage = models.ImageField(upload_to = "img/%y")
class Event(models.Model):
    event_title  = models.TextField(max_length=100, verbose_name="Title")
    price  = models.TextField(max_length=100, verbose_name="Event Price")
    description  = models.TextField(verbose_name="Event Description", default = '')
    content_1  = models.TextField(verbose_name="Event Content 1", default='')
    content_2  = models.TextField(verbose_name="Event Content 2", default='')
    content_3  = models.TextField(verbose_name="Event Content 3", default='')
    content  = models.TextField(verbose_name="Event Summary")
    def __str__(self):
        return self.event_title

# specialImage = models.ImageField(upload_to = "img/%y")
class Special(models.Model):
    specialName = models.CharField(max_length=100,verbose_name ="Special Food Name")
    specialDescription =  models.TextField(verbose_name="Special Description")
    def __str__(self):
        return self.specialName
# chefImage = models.ImageField(upload_to = "img/%y")  
class Chef(models.Model):
    chefName = models.CharField(max_length=100,verbose_name ="Chef's Name")
    chefRole = models.CharField(max_length=100,verbose_name ="Chef's Role")
    def __str__(self):
        return self.chefName
class Reservation(models.Model):
    your_name = models.CharField(max_length = 50)
    your_phone = models.CharField(max_length = 50)
    your_email = models.EmailField(max_length = 50)
    date = models.DateField()
    time = models.TimeField()
    number_of_people = models.IntegerField()
    message = models.CharField(max_length = 2000)
    def __str__(self):
        return self.your_email

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    name = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50)
    location = models.CharField(max_length = 50)
    starterItems = models.ManyToManyField('StarterMenu', related_name='order', blank=True)
    mainItems = models.ManyToManyField('MainMenu', related_name='order', blank=True)
    dessertItems = models.ManyToManyField('DessertMenu', related_name='order', blank=True)
    drinkItems = models.ManyToManyField('DrinksMenu', related_name='order', blank=True)
    def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %Y %I:%M %p")}'