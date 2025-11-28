from django.http import HttpResponse  # pyright: ignore[reportMissingImports]
from django.template import loader  # pyright: ignore[reportMissingImports]
from django.db.models import Q  # pyright: ignore[reportMissingImports]
from django.shortcuts import get_object_or_404  # pyright: ignore[reportMissingImports]
from .models import Aprendiz



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
    data = Aprendiz.objects.all().values('id', 'documento_identidad', 'nombre', 'apellido', 'correo_electronico', 'telefono', 'programa_formacion', 'fecha_nacimiento')
    context = {
        "aprendices": data,
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