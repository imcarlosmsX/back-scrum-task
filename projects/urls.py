from rest_framework import routers
from .api import *
router = routers.DefaultRouter()

router.register('usuario', usuarioViewSet, 'usuario')
router.register('equipoTrabajo', equipoTrabajoViewSet, 'equipoTrabajo')
router.register('roles', rolesViewSet, 'roles')
router.register('proyecto', proyectoViewSet, 'proyecto')
router.register('usuarioEquipo', usuarioEquipoViewSet, 'usuarioEquipo')
router.register('tarea', tareaViewSet, 'tarea')
router.register('sprint', sprintViewSet, 'sprint')
router.register('comentario', comentarioViewSet, 'comentario')

urlpatterns = router.urls