from django import forms

class HelloForm(forms.Form):
  name = forms.CharField(label='name', required=True, widget = forms.TextInput(attrs={'class':'form-control'}))
  mail = forms.EmailField(label='mail', widget = forms.EmailInput(attrs={'class':'form-control'}))
  age = forms.IntegerField(label='age', widget = forms.NumberInput(attrs={'class':'form-control'}))