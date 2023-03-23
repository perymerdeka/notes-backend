from django.urls import path, include

from apps.notes.api.routes import router
from apps.notes.views import index
urlpatterns = [
    path("", index)
] + router.urls