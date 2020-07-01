from django import forms
from .models import Appointment


class CreateAppointment(forms.ModelForm):
    class Meta: 
        model = Appointment
        fields=('title', 'content',)
        exclude=('publisher',)

class SearchForm(forms.ModelForm):
     word = forms.CharField(label='Search Word')
