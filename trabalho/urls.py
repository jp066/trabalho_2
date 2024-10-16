from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('auth/', include('authentication.urls')),
    path('professor/', include('professor.urls')),
    path('turma/', include('turma.urls')),
    ]