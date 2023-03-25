from django.db import models

# Create your models here.
class NotesModel(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    note = models.TextField()
    is_completed = models.BooleanField(default=False)
    date = models.DateField()
    startTime = models.DateField()
    endTime = models.DateTimeField()
    color = models.IntegerField()
    remind = models.BooleanField(default=False)
    repeat = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title