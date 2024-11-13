from .models import *
from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegistroUsuarioSerializer

class usuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = usuarioSerializer

class equipoTrabajoViewSet(viewsets.ModelViewSet):
    queryset = EquipoTrabajo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = equipoTrabajoSerializer

class rolesViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = rolesSerializer

class proyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = proyectoSerializer

class usuarioEquipoViewSet(viewsets.ModelViewSet):
    queryset = UsuarioEquipo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = usuarioEquipoSerializer

class tareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = tareaSerializer

class sprintViewSet(viewsets.ModelViewSet):
    queryset = Sprint.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = sprintSerializer

class comentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = comentarioSerializer

class RegistroUsuarioView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = RegistroUsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
