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
    
