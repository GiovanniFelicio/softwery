from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'login', 'dateBirth']    


class DateInput(forms.DateInput):
    input_type = 'date'

class UserCreateForm(forms.Form):
    name = forms.CharField(max_length=100, 
                           label='Name:',
                           widget=forms.TextInput(attrs={
                               'class':'form-control'
                           }))
    
