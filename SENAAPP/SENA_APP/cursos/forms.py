from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = [
            'codigo',
            'nombre',
            'programa',
            'instructor_coordinador',
            'fecha_inicio',
            'fecha_fin',
            'horario',
            'aula',
            'cupos_maximos',
            'estado',
            'observaciones',
        ]

        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'programa': forms.Select(attrs={'class': 'form-control'}),
            'instructor_coordinador': forms.Select(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'fecha_fin': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'horario': forms.TextInput(attrs={'class': 'form-control'}),
            'aula': forms.TextInput(attrs={'class': 'form-control'}),
            'cupos_maximos': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
        }

        labels = {
            'codigo': 'Código del Curso',
            'nombre': 'Nombre del Curso',
            'programa': 'Programa de Formación',
            'instructor_coordinador': 'Instructor Coordinador',
            'fecha_inicio': 'Fecha de Inicio',
            'fecha_fin': 'Fecha de Finalización',
            'horario': 'Horario',
            'aula': 'Aula/Ambiente',
            'cupos_maximos': 'Cupos Máximos',
            'estado': 'Estado del Curso',
            'observaciones': 'Observaciones',
        }
