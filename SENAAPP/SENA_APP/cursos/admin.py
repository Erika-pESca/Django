from django.contrib import admin
from .models import Curso, AprendizCurso, InstructorCurso

admin.site.register(Curso)
admin.site.register(InstructorCurso)
admin.site.register(AprendizCurso)