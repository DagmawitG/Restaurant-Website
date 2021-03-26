from django.db import models

class Hero(models.Model):
    restaurantName = models.CharField(max_length=100)
    restaurantMotto = models.TextField()
    def __str__(self):
        return self.restaurantName

class About(models.Model):
    aboutTitle = models.CharField(max_length=100)
    aboutPar1 = models.TextField()
    aboutPar2 = models.TextField()
    aboutPar3 = models.TextField()
    def __str__(self):
        return self.aboutTitle

class WhyUs(models.Model):
    whyUsTitle = models.CharField(max_length=100)
    whyUs1 = models.CharField(max_length=100)
    whyUsDesc1 = models.TextField()
    whyUs2 = models.CharField(max_length=100)
    whyUsDesc2 = models.TextField()
    whyUs3 = models.CharField(max_length=100)
    whyUsDesc3 = models.TextField()
    def __str__(self):
        return self.whyUsTitle

class Footer(models.Model):
    footerTitle = models.CharField(max_length=100)
    footerBody = models.CharField(max_length=200)
    twitterLink = models.TextField(max_length=100)
    facebookLink = models.TextField(max_length=100)
    instagramLink = models.TextField(max_length=100)
    linkedinLink = models.TextField(max_length=100)
    year = models.TextField(max_length=100, default='2021')
    copyrightText = models.TextField(max_length=100)
    def __str__(self):
        return self.footerTitle

class Location(models.Model):
    avenue = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    def __str__(self):
        return self.avenue +" " + self.city +", "+ self.country

class OpenHours(models.Model):
    weekdays_startTime  = models.CharField(max_length=100)
    weekdays_endTime = models.CharField(max_length=100)
    weekends_startTime  = models.CharField(max_length=100)
    weekends_endTime = models.CharField(max_length=100)
    def __str__(self):
        return self.weekdays_startTime +" " + self.weekdays_endTime + ", " + self.weekends_startTime+ " " + self.weekends_endTime

class Email(models.Model):
    email_address  = models.TextField(max_length=100)
    def __str__(self):
        return self.email_address

class Call(models.Model):
    phone_number  = models.TextField(max_length=100)
    def __str__(self):
        return self.phone_number

class StarterMenu(models.Model):
    starterOption = models.CharField(max_length=100)
    starterContent = models.CharField(max_length=100)
    starterDesc = models.TextField()
    starterPrice = models.CharField(max_length=100)
    def __str__(self):
        return self.starterContent
    
class MainMenu(models.Model):
    mainOption = models.CharField(max_length=100)
    mainContent = models.CharField(max_length=100)
    mainDesc = models.TextField()
    mainPrice = models.CharField(max_length=100)
    def __str__(self):
        return self.mainContent
    
class DessertMenu(models.Model):
    dessertOption = models.CharField(max_length=100)
    dessertContent = models.CharField(max_length=100)
    dessertDesc = models.TextField()
    dessertPrice = models.CharField(max_length=100)


    def __str__(self):
        return self.dessertContent
    
class DrinksMenu(models.Model):
    drinksOption = models.CharField(max_length=100)
    drinksContent = models.CharField(max_length=100)
    drinksDesc = models.TextField()
    drinksPrice = models.CharField(max_length=100)
    def __str__(self):
        return self.drinksContent
    
