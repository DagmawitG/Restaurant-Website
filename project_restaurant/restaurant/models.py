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



