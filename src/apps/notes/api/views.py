from rest_framework.viewsets import ModelViewSet

from apps.notes.models import NotesModel
from apps.notes.api.serializers import NotesSerializer

class NotesViewSet(ModelViewSet):
    queryset = NotesModel.objects.all()
    serializer_class = NotesSerializer

    
