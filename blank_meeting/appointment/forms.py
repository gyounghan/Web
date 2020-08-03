from django import forms
from .models import Appointment
import datetime
import pytz
class CreateAppointment(forms.ModelForm):
    class Meta: 
        model = Appointment
        fields=('title', 'content', 'place', 'time')
        exclude=('publisher',)
        widgets = {
          'time': forms.DateInput(attrs={'type': 'date'})
        }
    
    def clean_time(self):
        time = self.cleaned_data.get('time')
        
        now = datetime.datetime.now()
        now = pytz.utc.localize(now)
        print(str(time) + " date : " + str(now))

        if time < now:
           raise forms.ValidationError("The date cannot be in the past!")
        return time

class SearchForm(forms.ModelForm):
     word = forms.CharField(label='Search Word')