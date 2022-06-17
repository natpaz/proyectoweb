from django import forms
from .models import Formulario, Cliente

class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = ['nombre','correo','asunto','mensaje']

        labels = {
            'nombre': 'Nombre',
            'correo': 'Correo',
            'asunto': 'Asunto',
            'mensaje': 'Mensaje',

        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.TextInput(attrs={'class': 'form-control'}),
            'asunto': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje': forms.TextInput(attrs={'class': 'form-control'}),

        }
