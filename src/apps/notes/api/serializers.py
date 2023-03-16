from rest_framework.serializers import ModelSerializer

from apps.notes.models import NotesModel


class NotesSerializer(ModelSerializer):
    class Meta:
        model = NotesModel
        fields = ['id', 'title', 'created_at', "color_id", "note_content"]