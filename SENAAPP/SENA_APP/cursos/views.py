from django.shortcuts import render
from django.template import loader
from .models import Curso
from django.http import HttpResponse

from .forms import CursoForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())
def cursos(request):
    cursos = Curso.objects.all().prefetch_related('aprendices', 'instructores', 'programa', 'instructor_coordinador')
    template = loader.get_template('curso_list.html')
    
    context = {
        'cursos': cursos,
        'total_cursos': cursos.count(),
    }
    
    return HttpResponse(template.render(context, request))

def detalle_curso(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    aprendices_curso = curso.aprendizcurso_set.all()
    instructores_curso = curso.instructorcurso_set.all()
    template = loader.get_template('detalle_curso.html')
    
    context = {
        'curso': curso,
        'aprendices_curso': aprendices_curso,
        'instructores_curso': instructores_curso,
    }
    
    return HttpResponse(template.render(context, request))

#CREAR CURSO
class CursoCreateView(generic.CreateView):   
    """Vista para crear un nuevo curso"""
    model = Curso
    form_class = CursoForm
    template_name = 'agregar_curso.html'
    success_url = reverse_lazy('cursos:cursos_list')
    
    def form_valid(self, form):
        """Mostrar mensaje de éxito al crear el curso"""
        messages.success(
            self.request,
            f'El curso {form.instance.__str__} ha sido registrado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Hubo un error al registrar el curso. Por favor, revise el formulario e intente nuevamente.'
        )
        return super().form_invalid(form)
    
#UPDATE - CURSOS
class CursoUpdateView(generic.UpdateView):
    """Vista para actualizar un curso existente"""
    model = Curso
    form_class = CursoForm
    template_name = 'editar_curso.html'
    success_url = reverse_lazy('cursos:cursos_list')
    pk_url_kwarg = 'curso_id'
    
    def form_valid(self, form):
        """Mostrar mensaje de éxito al actualizar el curso"""
        messages.success(
            self.request,
            f'El curso {form.instance.__str__} ha sido actualizado exitosamente.'
        )
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Mostrar mensaje de error si el formulario es inválido"""
        messages.error(
            self.request,
            'Hubo un error al actualizar el curso. Por favor, revise el formulario e intente nuevamente.'
        )
        return super().form_invalid(form)
    #delete - cursos
class CursoDeleteView(generic.DeleteView):
    """Vista para eliminar un curso existente"""
    model = Curso
    template_name = 'eliminar_curso.html'
    success_url = reverse_lazy('cursos:cursos_list')
    pk_url_kwarg = 'curso_id'
    
    def delete(self, request, *args, **kwargs):
        """Mostrar mensaje de éxito al eliminar el curso"""
        curso = self.get_object()
        messages.success(
            self.request,
            f'El curso {curso.__str__} ha sido eliminado exitosamente.'
        )
        return super().delete(request, *args, **kwargs)