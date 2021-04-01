from django.urls import path
from djreservation import urls as djreservation_urls
from . import views
from . import reservation
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='restaurant-home'),
    # path("reserve", reservation.MyObjectReservation.as_view()),
    path('reservation.html', views.reservation, name='reservation'),
]
