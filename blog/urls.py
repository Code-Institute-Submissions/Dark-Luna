from django.urls import path
# from . import views
from .views import BlogHomeView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', BlogHomeView.as_view(), name='blog'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
