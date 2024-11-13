from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import usuarioViewSet, equipoTrabajoViewSet, rolesViewSet, proyectoViewSet, RegistroUsuarioView, CustomTokenObtainPairView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register(r'usuarios', usuarioViewSet)
router.register(r'equipos', equipoTrabajoViewSet)
router.register(r'roles', rolesViewSet)
router.register(r'proyectos', proyectoViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="Documentación de la API para el proyecto",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/registro/', RegistroUsuarioView.as_view(), name='registro_usuario'),
    path('api/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('documentation/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]