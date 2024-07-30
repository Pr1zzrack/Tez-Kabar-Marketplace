from .views import *
from django.urls import path


urlpatterns = [
    path('cars/', CarViewSet.as_view({'get': 'list', 'post': 'create'}), name='cars_list'),
    path('car/<int:id>/', CarViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='car_detail'),
    # Марки
    path('marka/', MarkaViewSet.as_view({'get': 'list', 'post': 'create'}), name='marka_list'),
    path('marka/<int:id>/', MarkaViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='marka_detail'),
    # Кузовы
    path('bodys/', BodyViewSet.as_view({'get': 'list', 'post': 'create'}), name='body_list'),
    path('body/<int:id>/', BodyViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='body_detail'),
    # Цвета кузовов
    path('body-color/', BodyColorViewSet.as_view({'get': 'list', 'post': 'create'}), name='body_color_list'),
    path('body-color/<int:id>/', BodyColorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='body_color_detail'),
    # Информация для фильтрации (front-end)
    path('car-data/', CarDataView.as_view(), name='car-data'),
    # Checpoint
    path('checkpoint/', CheckpointViewSet.as_view({'get': 'list', 'post': 'create'}), name='checkpoint'),
    path('checkpoint/<int:id>/', CheckpointViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='checkpoint'),
    # Года
    path('year/', YearViewSet.as_view({'get': 'list', 'post': 'create'}), name='year'),
    path('year/<int:id>/', YearViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='year'),
    # DriveUnit
    path('drive-unit/', DriveUnitViewSet.as_view({'get': 'list', 'post': 'create'}), name='drive-unit'),
    path('drive-unit/<int:id>/', DriveUnitViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='drive-unit'),
    # streeng-whell
    path('streeng-whell/', StreengWhellViewSet.as_view({'get': 'list', 'post': 'create'}), name='streeng-whell'),
    path('streeng-whell/<int:id>/', StreengWhellViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='streeng-whell'),
    # Фото машины
    path('car-image/', CarImageViewSet.as_view({'get': 'list', 'post': 'create'}), name='car-image'),
    path('car-image/<int:id>/', CarImageViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='car-image'),
]
