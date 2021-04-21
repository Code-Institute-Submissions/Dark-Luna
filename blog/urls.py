from django.urls import path
from .views import (
     BlogHomeView, BlogDetailView, AddBlogPost, UpdatePostView,
     DeletePostView, CategoryView, AddCategoryView, LikeView, AddCommentView,
     UpdateCommentView, DeleteCommentView)
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

     path('like/<int:pk>', LikeView, name='like_post'),

     path('article/comment/<int:pk>/', AddCommentView.as_view(),
          name='add-comment'),

     path('article/comment/update/<int:pk>/', UpdateCommentView.as_view(),
          name='update-comment'),

     path('article/comment/delete/<int:pk>', DeleteCommentView.as_view(),
          name='delete-comment'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
