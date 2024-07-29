from .views import *
from django.urls import path


urlpatterns = [
    path('category/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category'),
    path('category/<int:id>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='category'),
    path('cars/', CarViewSet.as_view({'get': 'list', 'post': 'create'}), name='car'),
    path('cars/<int:id>/', CarViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='car'),
]
