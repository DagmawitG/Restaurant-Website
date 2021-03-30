from .models import *
<<<<<<< HEAD
from .forms import *

=======
from django.shortcuts import render, redirect
from .forms import ReservationForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
>>>>>>> 24a9e0af974d92b9aceaf47e1e72add9ce67b862

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

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            body = {
            'your_name': form.cleaned_data['your_name'], 
            'your_phone': form.cleaned_data['your_phone'], 
            'your_email': form.cleaned_data['your_email'], 
            'date': form.cleaned_data['date'], 
            'number_of_people': form.cleaned_data['number_of_people'], 
            'message':form.cleaned_data['message']
                }
            messages.success(request, 'Your reservation is now being processed, {name}!'.format(name = body['your_name']))
            return redirect('restaurant-home')
        else:
            messages.error(request, 'Reservation not created')

    else:
        form = ReservationForm()
    context1['form'] = form
    return render(request, "restaurant/reservation.html", context1)
