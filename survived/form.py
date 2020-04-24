from django import forms

class SearchForm(forms.Form):
    country = forms.CharField(label='country', max_length=100)
    province = forms.CharField(label='province', max_length=100)
