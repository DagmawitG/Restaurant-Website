from .models import *
from django.shortcuts import render, redirect
from .forms import *
from django.core.mail import send_mail


def home(request):
    context1 = {
        'heros' : Hero.objects.all(),
        'aboutUs': About.objects.all(),
        'whyUs': WhyUs.objects.all(),
        'footer': Footer.objects.all().first(),
        'location': Location.objects.all(),
        'openHours': OpeningHour.objects.all().first(),
        'email': Email.objects.all(),
        'call': Call.objects.all(),
        'starterMenu': StarterMenu.objects.all(),
        'mainMenu': MainMenu.objects.all(),
        'dessertMenu': DessertMenu.objects.all(),
        'drinksMenu': DrinksMenu.objects.all(),
        'testimonials': Testimonial.objects.all(),
        'events': Event.objects.all(),
        'specials': Special.objects.all(),
        'chefs':Chef.objects.all(),
        'specials': Special.objects.all(),
        'links': Link.objects.all().first()

    }    
    
    return render(request, 'restaurant/home.html',context1)


def reservation(request):
    
   
    if request.method == "POST":
        your_name = request.POST['name']
        your_phone = request.POST['phone']
        your_email = request.POST['email']
        date = request.POST['date']
        time = request.POST['time']
        number_of_people = request.POST['people']
        message = request.POST['message']
        
        reservation = "Name:" + your_name + " /n Phone:" + your_phone + "/n Email:" + your_email + "/n Date:" + date + "/n Time:" + time + " /n Number of People" + number_of_people + "/n Message:" + message
        send_mail(
            'Reservation Request',
            reservation,
            your_email,
            ['se.dagmawit.getachew@gmail.com'],
        )

        return render(request, 'restaurant/reservation.html', {
        'your_name':your_name,
        'your_phone':your_phone,
        'your_email':your_email,
        'date':date,
        'time':time,
        'number_of_people':number_of_people,
        'message':message, })
    else:
        return render(request, 'restaurant/home.html',{})

    

  
