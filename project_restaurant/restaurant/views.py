from .models import *
from django.shortcuts import render, redirect
from .forms import *
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.views import View

class Order(View):
    def get(self, request, *args, **kwargs):
        appetizers = StarterMenu.objects.filter(starterOption='Starter')
        entres = MainMenu.objects.filter(mainOption='Main')
        desserts = DessertMenu.objects.filter(dessertOption='Dessert')
        drinks = DrinksMenu.objects.filter(drinksOption='Drink')
        context = {
            'appetizers': appetizers,
            'entres': entres,
            'desserts': desserts,
            'drinks': drinks,
            'heros' : Hero.objects.all(),
            'links': Link.objects.all().first(),
            'footer': Footer.objects.all().first(),
        }
        return render(request, 'users/order.html', context)
    def post(self, request, *args, **kwargs):
        order_items = {
            'items': []
        }
        items = request.POST.getlist('items[]')
        for item in items:
            menu_item = MenuItem.objects.get(pk__contains=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price,
            }
            order_items['items'].append(item_data)
        
        price = 0
        item_ids = []
        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])
        
        order = OrderModel.objects.create(price=price)
        order.items.add(*item_ids)
        context = {
            'items': order_items['items'],
            'price': price,
            'heros' : Hero.objects.all(),
            'links': Link.objects.all().first(),
            'footer': Footer.objects.all().first(),
                
        }
        return render(request, 'users/order_confirmation.html', context)


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
