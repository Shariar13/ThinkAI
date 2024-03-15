from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('signin.urls')),
] + static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

admin.site.site_header = "ThinkAI Panel"
admin.site.site_title = "ThinkAI Admin Panel"
admin.site.index_title = "Welcome To ThinkAI"