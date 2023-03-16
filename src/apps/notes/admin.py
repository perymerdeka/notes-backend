from django.contrib import admin

# Register your models here.
from apps.notes.models import NotesModel

class NotesModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(NotesModel, NotesModelAdmin)
