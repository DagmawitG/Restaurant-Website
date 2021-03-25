from django.shortcuts import render
# from django.http import HttpResponse

def home(request):
    
    return render(request, 'restaurant/home.html')
def about(request):
    return render(request, 'restaurant/about.html', {'title': "About"})