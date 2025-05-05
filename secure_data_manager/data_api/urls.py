from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientDataViewSet

router = DefaultRouter()
router.register(r'patients', PatientDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]