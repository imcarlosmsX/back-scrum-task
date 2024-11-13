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

    @swagger_auto_schema(
        operation_description="Obtener todos los proyectos de un equipo específico.",
        responses={
            200: proyectoSerializer(many=True),
            400: 'Solicitud incorrecta',
            404: 'Equipo no encontrado'
        },
        manual_parameters=[
            openapi.Parameter('equipo_id', openapi.IN_QUERY, description="ID del equipo", type=openapi.TYPE_INTEGER)
        ]
    )
    @action(detail=False, methods=['get'])
    def getProyectosPerEquipo(self, request):
        equipo_id = request.query_params.get('equipo_id')
        if not equipo_id:
            return Response({'error': 'El parámetro equipo_id es requerido.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            proyectos = Proyecto.objects.filter(equipo_trabajo_id=equipo_id)
            serializer = proyectoSerializer(proyectos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except EquipoTrabajo.DoesNotExist:
            return Response({'error': 'Equipo no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

class usuarioEquipoViewSet(viewsets.ModelViewSet):
    queryset = UsuarioEquipo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = usuarioSerializer

    @swagger_auto_schema(
        operation_description="Obtener el equipo de trabajo de un usuario específico.",
        responses={
            200: equipoTrabajoSerializer(many=True),
            400: 'Solicitud incorrecta',
            404: 'Usuario no encontrado'
        },
        manual_parameters=[
            openapi.Parameter('usuario_id', openapi.IN_QUERY, description="ID del usuario", type=openapi.TYPE_INTEGER)
        ]
    )
    @action(detail=False, methods=['get'])
    def getEquipoTrabajoPerUser(self, request):
        usuario_id = request.query_params.get('usuario_id')
        if not usuario_id:
            return Response({'error': 'El parámetro usuario_id es requerido.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            equipos = EquipoTrabajo.objects.filter(usuarioequipo__usuario_id=usuario_id)
            serializer = equipoTrabajoSerializer(equipos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Usuario.DoesNotExist:
            return Response({'error': 'Usuario no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

class tareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = tareaSerializer

    @swagger_auto_schema(
        operation_description="Obtener todas las tareas de un sprint específico.",
        responses={
            200: tareaSerializer(many=True),
            400: 'Solicitud incorrecta',
            404: 'Sprint no encontrado'
        },
        manual_parameters=[
            openapi.Parameter('sprint_id', openapi.IN_QUERY, description="ID del sprint", type=openapi.TYPE_INTEGER)
        ]
    )
    @action(detail=False, methods=['get'])
    def getTareaPerSprint(self, request):
        sprint_id = request.query_params.get('sprint_id')
        if not sprint_id:
            return Response({'error': 'El parámetro sprint_id es requerido.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            tareas = Tarea.objects.filter(sprint_id=sprint_id)
            serializer = tareaSerializer(tareas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Sprint.DoesNotExist:
            return Response({'error': 'Sprint no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

class sprintViewSet(viewsets.ModelViewSet):
    queryset = Sprint.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = sprintSerializer

    @swagger_auto_schema(
        operation_description="Obtener todos los sprints de un proyecto específico.",
        responses={
            200: sprintSerializer(many=True),
            400: 'Solicitud incorrecta',
            404: 'Proyecto no encontrado'
        },
        manual_parameters=[
            openapi.Parameter('proyecto_id', openapi.IN_QUERY, description="ID del proyecto", type=openapi.TYPE_INTEGER)
        ]
    )
    @action(detail=False, methods=['get'])
    def getSprintsPerProyecto(self, request):
        proyecto_id = request.query_params.get('proyecto_id')
        if not proyecto_id:
            return Response({'error': 'El parámetro proyecto_id es requerido.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            sprints = Sprint.objects.filter(proyecto_id=proyecto_id)
            serializer = sprintSerializer(sprints, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Proyecto.DoesNotExist:
            return Response({'error': 'Proyecto no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

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
