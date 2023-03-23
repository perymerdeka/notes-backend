from rest_framework.routers import DefaultRouter

from apps.notes.api.views import NotesViewSet

router = DefaultRouter()
router.register("notes", NotesViewSet)