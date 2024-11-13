from .models import *
from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegistroUsuarioSerializer, CustomTokenObtainPairSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import action

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
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = usuarioEquipoSerializer

    @swagger_auto_schema(
        operation_description="Obtener los equipos de trabajo asociados al usuario autenticado.",
        responses={
            200: equipoTrabajoSerializer(many=True),
            401: 'No autenticado',
            404: 'Usuario no encontrado o sin equipos asociados'
        },
        security=[{'Bearer': []}]
    )
    @action(detail=False, methods=['get'])
    def getEquipoTrabajoPerUser(self, request):
        user = request.user

        equipos = EquipoTrabajo.objects.filter(
            id__in=UsuarioEquipo.objects.filter(usuario=user).values_list('equipo_trabajo_id', flat=True)
        )
        if not equipos.exists():
            return Response({'error': 'Usuario no encontrado o sin equipos asociados'}, status=404)

        serializer = equipoTrabajoSerializer(equipos, many=True)
        return Response(serializer.data)

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

    @swagger_auto_schema(
        request_body=RegistroUsuarioSerializer,
        responses={
            201: openapi.Response('Usuario creado exitosamente', RegistroUsuarioSerializer),
            400: 'Solicitud incorrecta'
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = RegistroUsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    @swagger_auto_schema(
        request_body=CustomTokenObtainPairSerializer,
        responses={
            200: openapi.Response('Token obtenido exitosamente'),
            400: 'Solicitud incorrecta'
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
