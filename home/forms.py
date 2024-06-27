from django import forms
from .models import Amodel

class Aforms (forms.ModelForm):
    class Meta:
        model = Amodel
        fields = [ 'name','email','password'] 

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'})

        }