from django import forms
from .models import Programa

class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa
        fields = [
            'codigo',
            'nombre',
            'modalidad',
            'descripcion',
            'competencias',
            'nivel_formacion',
            'duracion_meses',
            'requisitos_ingreso',
            'centro_formacion',
            'estado',
        ]

        widgets = {
            'codigo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el código del programa'
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre del programa'
            }),
            'modalidad': forms.Select(attrs={
                'class': 'form-control',
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción del programa',
                'rows': 4
            }),
            'competencias': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Competencias del programa',
                'rows': 4
            }),
            'nivel_formacion': forms.Select(attrs={
                'class': 'form-control'
            }),
            'duracion_meses': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Duración en meses'
            }),
            'requisitos_ingreso': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Requisitos de ingreso'
            }),
            'centro_formacion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Centro de formación'
            }),
            'estado': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

        labels = {
            'codigo': 'Código del Programa',
            'nombre': 'Nombre del Programa',
            'modalidad': 'Modalidad',
            'competencias': 'Competencias',
            'descripcion': 'Descripción',
            'nivel_formacion': 'Nivel de Formación',
            'duracion_meses': 'Duración (meses)',
            'requisitos_ingreso': 'Requisitos de Ingreso',
            'centro_formacion': 'Centro de Formación',
            'estado': 'Estado',
        }
