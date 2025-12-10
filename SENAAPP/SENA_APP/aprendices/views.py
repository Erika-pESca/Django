from django.http import HttpResponse  # pyright: ignore[reportMissingImports]
from django.template import loader  # pyright: ignore[reportMissingImports]
from django.db.models import Q  # pyright: ignore[reportMissingImports]
from django.shortcuts import get_object_or_404  # pyright: ignore[reportMissingImports]
from .models import Aprendiz

from .forms import AprendizForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages



# Create your views here.
def main(request):
    total_aprendices = Aprendiz.objects.count()
    programas_count = Aprendiz.objects.values('programa_formacion').distinct().count()
    
    context = {
        'total_aprendices': total_aprendices,
        'programas_count': programas_count,
    }
    template = loader.get_template("main.html")
    return HttpResponse(template.render(context, request))


def aprendices_list(request):
    aprendices = Aprendiz.objects.all().values('id', 'documento_identidad', 'nombre', 'apellido', 'correo_electronico', 'telefono', 'programa_formacion', 'fecha_nacimiento')
    context = {
        "aprendices": aprendices,
    }

    template = loader.get_template('aprendices_list.html')
    return HttpResponse(template.render(context, request))

def detalle_aprendiz(request, aprendiz_id):
    aprendiz = get_object_or_404(Aprendiz, id=aprendiz_id) #Datos
    template = loader.get_template('detalle_aprendiz.html') #Template
    context = {
        'aprendiz': aprendiz,
    }
    
    return HttpResponse(template.render(context, request))

    # VISTAS BASADAS EN CLASES - CRUD APRENDIZ

# CREATE - APRENDIZ

class AprendizCreateView(generic.CreateView):
    """Vista para crear un nuevo aprendiz"""
    model = Aprendiz
    form_class = AprendizForm
    template_name = 'agregar_aprendiz.html'
    success_url = reverse_lazy('aprendices:aprendices')
    
    def form_valid(self, form):
        """Mostrar mensaje de éxito al crear el aprendiz"""
        messages.success(
            self.request,
            f'El aprendiz {form.instance.nombre_completo()} ha sido registrado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)


# UPDATE - APRENDIZ
class AprendizUpdateView(generic.UpdateView):
    """Vista para actualizar un aprendiz existente"""
    model = Aprendiz
    form_class = AprendizForm
    template_name = 'editar_aprendiz.html'
    success_url = reverse_lazy('aprendices:aprendices_list')
    pk_url_kwarg = 'aprendiz_id'
    
    def form_valid(self, form):
        """Mostrar mensaje de éxito al actualizar"""
        messages.success(
            self.request,
            f'El aprendiz {form.instance.nombre_completo()} ha sido actualizado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Por favor, corrija los errores en el formulario.'
        )
        return super().form_invalid(form)


# DELETE - APRENDIZ
class AprendizDeleteView(generic.DeleteView):
    """Vista para eliminar un aprendiz"""
    model = Aprendiz
    template_name = 'eliminar_aprendiz.html'
    success_url = reverse_lazy('aprendices:aprendices_list')
    pk_url_kwarg = 'aprendiz_id'
    
    def delete(self, request, *args, **kwargs):
        """Mostrar mensaje de éxito al eliminar"""
        aprendiz = self.get_object()
        messages.success(
            request,
            f'El aprendiz {aprendiz.nombre_completo()} ha sido eliminado exitosamente.'
        )
        return super().delete(request, *args, **kwargs)