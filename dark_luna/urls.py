"""dark_luna URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('why/', include('why.urls')),
    path('how/', include('how.urls')),
    path('life/', include('life.urls')),
    path('sex/', include('sex.urls')),
    path('shadow/', include('shadow.urls')),
    path('massage/', include('massage.urls')),
    path('workshops/', include('workshops.urls')),
    path('blog/', include('blog.urls')),
    path('therapists/', include('therapists.urls')),
    path('contact/', include('contact.urls')),
    path('account/', include('profiles.urls')),
    path('booking/', include('booking.urls')),
    path('checkout/', include('checkout.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
