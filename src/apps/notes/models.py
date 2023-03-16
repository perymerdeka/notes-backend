from django.db import models

# Create your models here.
class NotesModel(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    color_id = models.IntegerField()
    note_content = models.TextField()

    def __str__(self) -> str:
        return self.title