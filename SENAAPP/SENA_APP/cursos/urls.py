from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('cursos/', views.cursos, name='cursos'),
    path("cursos/<int:curso_id>", views.detalle_curso, name="detalle_curso"),
]
