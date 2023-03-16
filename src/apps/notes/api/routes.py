from rest_framework.routers import DefaultRouter

from .views import NotesViewSet

router: DefaultRouter = DefaultRouter()

router.register(r"notes", NotesViewSet)

