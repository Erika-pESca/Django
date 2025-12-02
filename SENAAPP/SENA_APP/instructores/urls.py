from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('instructores/', views.instructores, name='instructores'),
    path("instructores/<int:instructor_id>", views.detalle_instructor, name="detalle_instructor"),
]