from django.urls import path
from .views import AddTestimonial
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('add_testimonial/', AddTestimonial.as_view(),
         name='add-testimonial'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
