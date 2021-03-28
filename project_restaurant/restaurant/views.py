from .models import *
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

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


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry" 
            body = {
                'first_name': form.cleaned_data['first_name'], 
                'last_name': form.cleaned_data['last_name'], 
                'email': form.cleaned_data['email_address'], 
                'message':form.cleaned_data['message']
            }
            message = "\n".join(body.values())
            
            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            messages.success(request, 'Your message is sent')
            return redirect('restaurant-home')
        else:
            messages.error(request, 'Message not sent')

    else:
        form = ContactForm()
    return render(request, "restaurant/home.html", {'form':form})
