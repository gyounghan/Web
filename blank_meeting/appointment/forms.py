from django import forms
from .models import Appointment
from .models import Notification
import datetime

class CreateAppointment(forms.ModelForm):
    class Meta: 
        renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

        model = Appointment
        fields=('title', 'content', 'place', 'time',)
        exclude=('publisher',)

    date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.date.today():
           raise forms.ValidationError("The date cannot be in the past!")
        return date

class SearchForm(forms.ModelForm):
     word = forms.CharField(label='Search Word')

class CreateNotification(forms.ModelForm):
    class Meta:
        model = Notification
        fields=('message',)
        exclude=('sender', 'receiver', 'appointment',)
