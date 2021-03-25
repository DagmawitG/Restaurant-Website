from django.shortcuts import render
# from django.http import HttpResponse
from .models import Hero,About,WhyUs

def home(request):
    context1 = {
        'heros' : Hero.objects.all(),

        'aboutUs': About.objects.all(),

        'whyUs': WhyUs.objects.all()
    }
    
    return render(request, 'restaurant/home.html',context1)
    
def about(request):
    return render(request, 'restaurant/about.html', {'title': "About"})