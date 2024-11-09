from rest_framework import serializers
from .models import *

class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class equipoTrabajoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipoTrabajo
        fields = '__all__'


class rolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'


class proyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = '__all__'

class usuarioEquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioEquipo
        fields = '__all__'

class tareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'


class sprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = '__all__'

class comentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'
