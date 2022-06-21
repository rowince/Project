from django.db import router
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stud', views.StudSerializers, basename='student')

urlpatterns = [
    path('', include(router.urls)),
]
