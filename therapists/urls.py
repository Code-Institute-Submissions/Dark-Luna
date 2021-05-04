from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='therapists'),

    path('admin/therapists-page/therapists',
         views.therapists_admin, name='therapists_admin'),

    path('admin/therapists-page/therapists/add/',
         views.add_therapist_admin, name='add_therapist_admin'),

    path('admin/therapists-page/therapist/edit/<int:therapist_id>',
         views.edit_therapist_admin, name='edit_therapist_admin'),

    path('admin/therapists-page/therapists/remove/<int:therapist_id>',
         views.remove_therapist_admin, name='remove_therapist_admin'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
