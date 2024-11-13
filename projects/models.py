from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class EquipoTrabajo(models.Model):
    nombre_equipo = models.CharField(max_length=255)
    descripcion_equipo = models.TextField()

    def __str__(self):
        return self.nombre_equipo


class Roles(models.Model):
    nombre_rol = models.CharField(max_length=100)
    descripcion_rol = models.TextField()
    equipo_trabajo = models.ForeignKey(EquipoTrabajo, on_delete=models.CASCADE, related_name="roles")

    def __str__(self):
        return f"{self.nombre_rol} - {self.equipo_trabajo.nombre_equipo}"


class Proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=255)
    descripcion_proyecto = models.TextField()
    fecha_inicio_proyecto = models.DateField(auto_now=True)
    fecha_fin_proyecto = models.DateField()
    estado_proyecto = models.CharField(max_length=50)
    equipo_trabajo = models.ForeignKey(EquipoTrabajo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_proyecto


class UsuarioEquipo(models.Model):
    usuario_equipo_id = models.AutoField(primary_key=True)
    fecha_union = models.DateField(auto_now=True)
    rol_equipo = models.CharField(max_length=100, default="Owner")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    equipo_trabajo = models.ForeignKey(EquipoTrabajo, on_delete=models.CASCADE)
    es_creador = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.usuario} - {self.equipo_trabajo} - Creador: {self.es_creador}"


class Sprint(models.Model):
    nombre_sprint = models.CharField(max_length=255)
    fecha_inicio = models.DateField(auto_now=True)
    fecha_fin = models.DateField()
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_sprint


class Tarea(models.Model):
    nombre_tarea = models.CharField(max_length=255)
    descripcion_tarea = models.TextField()
    fecha_inicio_tarea = models.DateField(auto_now=True)
    fecha_fin_tarea = models.DateField()
    estado_tarea = models.CharField(max_length=50)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, related_name="tareas")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_tarea
    
class Comentario(models.Model):
    contenido_comentario = models.TextField()
    fecha_comentario = models.DateField(auto_now=True)
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comentario by {self.usuario} on Tarea {self.tarea}"
