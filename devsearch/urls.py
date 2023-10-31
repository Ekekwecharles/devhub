from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("projects/", include('projects.urls')),
    path('', include('users.urls')),

    path('reset_password/', auth_views.PasswordResetView.as_view(), 
         name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), 
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), 
         name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), 
         name="password_reset_complete")

]



# keeping the main URL routing patterns separate from the static file serving pattern
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# static() is used to ser.ve static files (such as CSS, JavaScript, and images) during development.
# It's a utility function provided by Django that generates URL patterns for serving static files from a specified directory on your local file system.

# For production
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)