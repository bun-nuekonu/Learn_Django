from django import forms

# class HelloForm(forms.Form):
#   data =[
#     ('one', 'item 1'),
#     ('two', 'item 2'),
#     ('three', 'item 3')
#   ]
#   choice = forms.MultipleChoiceField(label='radio', choices=data, widget=forms.SelectMultiple(attrs={'size':3, 'class':'form-select'}))

class SessionForm(forms.Form):
  session = forms.CharField(label='session', required=False, widget=forms.TextInput(attrs={'class':'form-control'}))