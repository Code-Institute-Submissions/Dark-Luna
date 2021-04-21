from django.urls import path
from . import views
from .views import (
                    TestimonialHomeView,
                    AddTestimonialView,
                    UpdateTestimonialView,
                    DeleteTestimonialView)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.user_account, name='user_account'),
    path('testimonial/', TestimonialHomeView.as_view(), name='testimonial'),
    path('add_testimonial/', AddTestimonialView.as_view(),
         name='add-testimonial'),
    path('testimonial/update/<int:pk>',
         UpdateTestimonialView.as_view(), name='update-testimonial'),
    path('testimonial/delete/<int:pk>',
         DeleteTestimonialView.as_view(), name='delete-testimonial'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
