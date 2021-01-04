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
    
def form_options(required: bool, maxlength: int, rstrip: bool = False):
    options = {}
    options['required'] = bool(required)
    options['maxlength'] = int(maxlength)
    options['rstrip'] = bool(rstrip)
    
    return options
    
def form_create_user():
    form = {}
    
    form['name'] = form_options(True, 100, True)
    form['email'] = form_options(True, 255,True)
    form['login'] = form_options(True, 255,True)
    form['number'] = form_options(False, 20, True)
    form['dateBirth'] = form_options(True, 20, True)
    form['password'] = form_options(True, 20, True)
    form['company'] = form_options(True, -1, True)
    
    return form