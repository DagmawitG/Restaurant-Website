from django.shortcuts import render
# from django.http import HttpResponse
from .models import Hero,About,WhyUs,Footer

def home(request):
    context1 = {
        'heros' : Hero.objects.all(),

        'aboutUs': About.objects.all(),

        'whyUs': WhyUs.objects.all(),

        
        'footer': Footer.objects.all().first()
    }
    
    return render(request, 'restaurant/home.html',context1)
    
def about(request):
    return render(request, 'restaurant/about.html', {'title': "About"})