from django.urls import path
from . import views
from .views import (
     BlogHomeView, BlogDetailView, AddBlogPost, UpdatePostView,
     DeletePostView, LikeView, AddCommentView)
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

     path('add_category',
          views.categories, name='categories_management'),

     path('category/edit/<int:category_id>',
          views.edit_categories, name='edit_category'),

     path('management/lessons-page/categories/remove/<int:category_id>',
          views.remove_categories, name='remove_category'),

     path('like/<int:pk>', LikeView, name='like_post'),

     path('article/comment/<int:pk>/', AddCommentView.as_view(),
          name='add-comment'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
