from djreservation.views import ProductReservationView
from .models import Reservation

class MyObjectReservation(ProductReservationView):
        base_model = Reservation     # required
        amount_field = 'quantity' # required
        extra_display_field = ['measurement_unit'] # not required