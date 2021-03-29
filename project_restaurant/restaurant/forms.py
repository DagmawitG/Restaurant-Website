from django import forms

class contactformemail(forms.Form):
    formemail = forms.EmailField(required = True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget= forms.Textarea,required=True)