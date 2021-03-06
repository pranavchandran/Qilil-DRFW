"""mysite URL Configuration

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
from rest_framework import routers
from foodapp.views import FoodViewSet, SweetViewSet, SpicyViewSet, RateViewSet
from django.conf.urls.static import static
from django.conf import settings

from foodapp.models import Foods
from django_filters.views import FilterView
from django_filters.views import object_filter


router = routers.SimpleRouter()
router.register('foods', FoodViewSet)
router.register('sweet', SweetViewSet)
router.register('spicy', SpicyViewSet)
# router.register('range', RateViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('foodapi/', RateViewSet.as_view()),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
