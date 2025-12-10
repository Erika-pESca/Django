from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Instructor
from django.shortcuts import get_object_or_404 
from django.db.models import Q

from .forms import InstructorForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

def main(request):
    total_Instructores = Instructor.objects.count()
    programas_count = Instructor.objects.values('programa_formacion').distinct().count()
    
    context = {
        'total_Instructores': total_Instructores,
        'programas_count': programas_count,}
    template = loader.get_template("main.html")
    return HttpResponse(template.render(context, request))


def instructores(request):
    myinstructores = Instructor.objects.all().values()
    context = {
        'myinstructores': myinstructores,
        
        }
    template = loader.get_template('instructores_list.html')
    return HttpResponse(template.render(context, request))
def detalle_instructor(request, instructor_id):
    instructor = get_object_or_404(Instructor, id=instructor_id) #
    template = loader.get_template('detalle_instructor.html')
    context = {
        'instructor': instructor,
    }
    return HttpResponse(template.render(context, request))

#CREAR INSTRUCTOR
class InstructorCreateView(generic.CreateView):
    """Vista para crear un nuevo instructor"""
    model = Instructor
    form_class = InstructorForm
    template_name = 'agregar_instructor.html'
    success_url = reverse_lazy('instructores:instructores_list')
    
    def form_valid(self, form):
        """Mostrar mensaje de éxito al crear el instructor"""
        messages.success(
            self.request,
            f'El instructor {form.instance.get_full_name()} ha sido registrado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Hubo un error al registrar el instructor. Por favor, verifique los datos e intente nuevamente.'
        )
        return super().form_invalid(form)
    
    #Update - Instructor
class InstructorUpdateView(generic.UpdateView):
    """Vista para actualizar los datos de un instructor existente"""
    model = Instructor
    form_class = InstructorForm
    template_name = 'editar_instructor.html'
    success_url = reverse_lazy('instructores:instructores_list')
    pk_url_kwarg = 'instructor_id'
    
    def form_valid(self, form):
        """Mostrar mensaje de éxito al actualizar el instructor"""
        messages.success(
            self.request,
            f'Los datos del instructor {form.instance.get_full_name()} han sido actualizados exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Hubo un error al actualizar los datos del instructor. Por favor, verifique los datos e intente nuevamente.'
        )
        return super().form_invalid(form)
    
# Delete - Instructor
class InstructorDeleteView(generic.DeleteView):
    """Vista para eliminar un instructor"""
    model = Instructor
    template_name = 'eliminar_instructor.html'
    success_url = reverse_lazy('instructores:instructores_list')
    pk_url_kwarg = 'instructor_id'
    
    def delete(self, request, *args, **kwargs):
        """Mostrar mensaje de éxito al eliminar el instructor"""
        instructor = self.get_object()
        messages.success(
            self.request,
            f'El instructor {instructor.get_full_name()} ha sido eliminado exitosamente.'
        )
        return super().delete(request, *args, **kwargs)
    