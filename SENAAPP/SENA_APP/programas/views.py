from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Programa
from django.shortcuts import get_object_or_404 
from django.db.models import Q

from .forms import ProgramaForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

def main(request):
    total_Programas = Programa.objects.count()
    programas_count = Programa.objects.values('programa_formacion').distinct().count()
    
    context = {
        'total_Programas': total_Programas,
        'programas_count': programas_count,}
    template = loader.get_template("main.html")
    return HttpResponse(template.render(context, request))


def programas(request):
    myprogramas = Programa.objects.all().values()
    context = {
        'myprogramas': myprogramas,
        
        }
    template = loader.get_template('programas_list.html')
    return HttpResponse(template.render(context, request))
def detalle_programa(request, programa_id):
    programa = get_object_or_404(Programa, id=programa_id) #
    template = loader.get_template('detalle_programa.html')
    context = {
        'programa': programa,
    }
    return HttpResponse(template.render(context, request))


#CREAR PROGRAMA
class ProgramaCreateView(generic.CreateView):   
    """Vista para crear un nuevo programa"""
    model = Programa
    form_class = ProgramaForm
    template_name = 'agregar_programa.html'
    success_url = reverse_lazy('programas:programas')
    
    def form_valid(self, form):
        """Mostrar mensaje de éxito al crear el programa"""
        messages.success(
            self.request,
            f'El programa {form.instance.__str__} ha sido registrado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Hubo un error al registrar el programa. Por favor, verifique los datos e intente nuevamente.'
        )
        return super().form_invalid(form)
    
    #update - programas
class ProgramaUpdateView(generic.UpdateView):
    """Vista para actualizar los datos de un programa existente"""
    model = Programa
    form_class = ProgramaForm
    template_name = 'editar_programa.html'
    success_url = reverse_lazy('programas:programas')
    pk_url_kwarg = 'programa_id'
    
    def form_valid(self, form):
        """Mostrar mensaje de éxito al actualizar el programa"""
        messages.success(
            self.request,
            f'El programa {form.instance.__str__} ha sido actualizado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Hubo un error al actualizar el programa. Por favor, verifique los datos e intente nuevamente.'
        )
        return super().form_invalid(form)
    
    #delete - programas
class ProgramaDeleteView(generic.DeleteView):
    """Vista para eliminar un programa existente"""
    model = Programa
    template_name = 'eliminar_programa.html'
    success_url = reverse_lazy('programas:programas')
    pk_url_kwarg = 'programa_id'
    
    def delete(self, request, *args, **kwargs):
        """Mostrar mensaje de éxito al eliminar el programa"""
        programa = self.get_object()
        messages.success(
            self.request,
            f'El programa {programa.__str__} ha sido eliminado exitosamente.'
        )
        return super().delete(request, *args, **kwargs)