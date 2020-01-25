from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = 'blog'
urlpatterns = [
    path('', blog_views, name='post'),
    path('blog/', blog_detail, name='detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
