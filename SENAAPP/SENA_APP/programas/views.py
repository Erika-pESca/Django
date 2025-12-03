from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Programa
from django.shortcuts import get_object_or_404 
from django.db.models import Q

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