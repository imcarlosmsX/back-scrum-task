from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import usuarioViewSet, equipoTrabajoViewSet, rolesViewSet, proyectoViewSet, RegistroUsuarioView

router = DefaultRouter()
router.register(r'usuarios', usuarioViewSet)
router.register(r'equipos', equipoTrabajoViewSet)
router.register(r'roles', rolesViewSet)
router.register(r'proyectos', proyectoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/registro/', RegistroUsuarioView.as_view(), name='registro_usuario'),
]