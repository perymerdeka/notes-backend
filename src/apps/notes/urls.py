from django.urls import path, include

from apps.notes.api.routes import router

urlpatterns = [
    
] + router.urls