from django.urls import path
from django.conf.urls import include, url
from djreservation import urls as djreservation_urls
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='restaurant-home'),
    path('reservation', views.reservation, name='reservation'),
    path('/paypal-return/', views.PaypalReturnView.as_view(), name='paypal-return'),
    path('/paypal-cancel/', views.PaypalCancelView.as_view(), name='paypal-cancel'),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('order/', views.Order.as_view(), name='order'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
