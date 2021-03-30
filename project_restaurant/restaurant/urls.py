from django.urls import path
from djreservation import urls as djreservation_urls
from . import views
from . import reservation
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='restaurant-home'),
    path("reserve", reservation.MyObjectReservation.as_view()),
    path('reservation', views.reservation, name='reservation'),
    path('order/', views.Order.as_view(), name='order'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
