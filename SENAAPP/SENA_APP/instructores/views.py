from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Instructor
from django.shortcuts import get_object_or_404 
from django.db.models import Q

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