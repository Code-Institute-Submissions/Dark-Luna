from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.user_account, name='user_account'),

    path('booking/review/<order_number>',
         views.booking_review, name='booking_review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
