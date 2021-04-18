from django.urls import path
from .views import (
     BlogHomeView, BlogDetailView, AddBlogPost, UpdatePostView,
     DeletePostView, CategoryView, AddCategoryView)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
     path('', BlogHomeView.as_view(), name='blog'),

     path('article/<int:pk>', BlogDetailView.as_view(),
          name='blog-post-detail'),

     path('add_post/', AddBlogPost.as_view(),
          name='add-blog-post'),

     path('article/update/<int:pk>', UpdatePostView.as_view(),
          name='update-blog-post'),

     path('article/delete/<int:pk>', DeletePostView.as_view(),
          name='delete_post'),

     path('add_category/', AddCategoryView.as_view(),
          name='add-blog-category'),

     path('category/<str:cats>/', CategoryView, name='category'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
