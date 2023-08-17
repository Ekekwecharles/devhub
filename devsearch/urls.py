from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("projects/", include('projects.urls')),
    path('', include('users.urls')),
]



# keeping the main URL routing patterns separate from the static file serving pattern
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# static() is used to serve static files (such as CSS, JavaScript, and images) during development.
# It's a utility function provided by Django that generates URL patterns for serving static files from a specified directory on your local file system.

# For production
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)