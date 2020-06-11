from django import forms

class SearchForm(forms.ModelForm):
     word = forms.CharField(label='Search Word')