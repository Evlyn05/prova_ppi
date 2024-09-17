from django.forms import ModelForm
from django import forms
from .models import Voo

class VooForm(ModelForm):
    class Meta:
        model = Voo
        fields = '__all__'
      
        widgets = {
            'origem' : forms.TextInput(attrs={'class': 'form-control' }),
            'destino': forms.TextInput(attrs={'class': 'form-control' }),
            'data_voo': forms.DateInput(attrs={'class': 'form-control', 'type': 'Date'}),
            'valor_passagem': forms.TextInput(attrs={'class': 'form-control' }),
            'companhia': forms.Select(attrs={'class': 'form-control' }),
        }