from django.urls import path
from . import views

app_name = 'programas'

urlpatterns = [
    path('', views.main, name='main'),
    path('programas/', views.programas, name='programas'),
    path("programas/<int:programa_id>", views.detalle_programa, name="detalle_programa"),
    path('programas/crear/', views.ProgramaCreateView.as_view(), name='crear_programa'),
    path('programas/<int:programa_id>/editar/', views.ProgramaUpdateView.as_view(), name='editar_programa'),
    path('programas/<int:programa_id>/eliminar/', views.ProgramaDeleteView.as_view(), name='eliminar_programa'),
]
