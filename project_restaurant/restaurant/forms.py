from django import forms
from .models import Reservation


# Create your forms here.

class ReservationForm(forms.Form):
    your_name = forms.CharField(max_length = 50)
    your_phone = forms.CharField(max_length = 50)
    your_email = forms.EmailField(max_length = 50)
    date = forms.DateField(max_length = 50)
    time = forms.TimeField(max_length = 50)
    number_of_people = forms.IntegerField(max_length = 50)
    message = forms.CharField(widget = forms.Textarea, max_length = 2000)

    class Meta:
        model = Reservation
        fields = ['your_name', 'your_phone', 'your_email', 'date', 'time', 'number_of_people', 'message']
