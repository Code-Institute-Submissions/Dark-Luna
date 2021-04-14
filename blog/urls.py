from django.urls import path
# from . import views
from .views import BlogHomeView, BlogDetailView, AddBlogPost
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', BlogHomeView.as_view(), name='blog'),
    path('article/<int:pk>', BlogDetailView.as_view(),
         name='blog-post-detail'),
    path('add_post/', AddBlogPost.as_view(),
         name='add-blog-post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
