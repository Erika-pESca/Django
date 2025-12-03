from django.db import models

class Curso(models.Model):
    ESTADO_CHOICES = [
        ('PRO', 'Programado'),
        ('INI', 'Iniciado'),
        ('EJE', 'En Ejecución'),
        ('FIN', 'Finalizado'),
        ('CAN', 'Cancelado'),
        ('SUS', 'Suspendido'),
    ]

    codigo = models.CharField(max_length=30, unique=True, verbose_name="Código del Curso")
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Curso")
    
    # Relaciones con otras Apps
    programa = models.ForeignKey('programas.Programa', on_delete=models.CASCADE, verbose_name="Programa de Formación")
    
    # Asegúrate de que la app 'instructores' y el modelo 'Instructor' existan
    instructor_coordinador = models.ForeignKey('instructores.Instructor', on_delete=models.CASCADE, related_name='cursos_coordinados', verbose_name="Instructor Coordinador")
    
    # Relaciones Muchos a Muchos con tablas intermedias (through)
    instructores = models.ManyToManyField('instructores.Instructor', through='InstructorCurso', related_name='cursos_impartidos', verbose_name="Instructores")
    aprendices = models.ManyToManyField('aprendices.Aprendiz', through='AprendizCurso', related_name='cursos', verbose_name="Aprendices")
    
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio")
    fecha_fin = models.DateField(verbose_name="Fecha de Finalización")
    horario = models.CharField(max_length=100, verbose_name="Horario")
    aula = models.CharField(max_length=50, verbose_name="Aula/Ambiente")
    cupos_maximos = models.PositiveIntegerField(verbose_name="Cupos Máximos")
    estado = models.CharField(max_length=3, choices=ESTADO_CHOICES, default='PRO', verbose_name="Estado del Curso")
    observaciones = models.TextField(blank=True, null=True, verbose_name="Observaciones")
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")

    def _str_(self):
        return f"{self.codigo} - {self.nombre}"