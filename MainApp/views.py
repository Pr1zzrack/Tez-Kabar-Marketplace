from django_filters.views import FilterView
from rest_framework import filters, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
import requests, django_filters
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.parsers import MultiPartParser, FormParser
from .models import *
from .serializers import *
from .filters import *

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'
    parser_classes = [MultiPartParser, FormParser]

class CarViewSet(viewsets.ModelViewSet, FilterView):
    queryset = Car.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = CarFilters
    lookup_field = 'id'
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return CarReadSerializer
        return CarWriteSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MarkaViewSet(viewsets.ModelViewSet):
    queryset = Marka.objects.all()
    serializer_class = MarkaSerializer
    lookup_field = 'id'
    # permission_classes = [AdminOnlyPermission]

class BodyViewSet(viewsets.ModelViewSet):
    queryset = Body.objects.all()
    serializer_class = BodySerializer
    lookup_field = 'id'
    # permission_classes = [AdminOnlyPermission]

class BodyColorViewSet(viewsets.ModelViewSet):
    queryset = BodyColor.objects.all()
    serializer_class = BodyColorSerializer
    lookup_field = 'id'
    # permission_classes = [AdminOnlyPermission]

class YearViewSet(viewsets.ModelViewSet):
    queryset = Year.objects.all()
    serializer_class = YearSerializer
    lookup_field = 'id'
    # permission_classes = [AdminOnlyPermission]

class DriveUnitViewSet(viewsets.ModelViewSet):
    queryset = DriveUnit.objects.all()
    serializer_class = DriveUnitSerializer
    lookup_field = 'id'
    # permission_classes = [AdminOnlyPermission]

class StreengWhellViewSet(viewsets.ModelViewSet):
    queryset = StreengWhell.objects.all()
    serializer_class = StreengWhellSerializer
    lookup_field = 'id'
    # permission_classes = [AdminOnlyPermission]

class CheckpointViewSet(viewsets.ModelViewSet):
    queryset = Checkpoint.objects.all()
    serializer_class = CheckpointSerializer
    lookup_field = 'id'
    # permission_classes = [AdminOnlyPermission]

class CarDataView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    @swagger_auto_schema(
        operation_summary="Получить все данные о машинах",
        responses={200: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'marka': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_OBJECT)),
                'body': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_OBJECT)),
                'body_color': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_OBJECT)),
                'year_of_manufacture_serializer': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_OBJECT)),
                'checkpoint_serializer': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_OBJECT)),
                'drive_unit_serializer': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_OBJECT)),
                'steering_wheel_serializer': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_OBJECT)),
            }
        )},
        tags=['Данные о машинах']
    )

    def get(self, request, format=None):
        marka_serializer = MarkaSerializer(Marka.objects.all(), many=True).data
        body_serializer = BodySerializer(Body.objects.all(), many=True).data
        body_color_serializer = BodyColorSerializer(BodyColor.objects.all(), many=True).data
        year_of_manufacture_serializer = YearSerializer(Year.objects.all(), many=True).data
        checkpoint_serializer = CheckpointSerializer(Checkpoint.objects.all(), many=True).data
        drive_unit_serializer = DriveUnitSerializer(DriveUnit.objects.all(), many=True).data
        steering_wheel_serializer = StreengWhellSerializer(StreengWhell.objects.all(), many=True).data
        return Response({
            'marka': marka_serializer,
            'body': body_serializer,
            'body_color': body_color_serializer,
            'year_of_manufacture': year_of_manufacture_serializer,
            'checkpoint': checkpoint_serializer,
            'drive_unit': drive_unit_serializer,
            'steering_wheel': steering_wheel_serializer,
        })

class CarImageViewSet(viewsets.ModelViewSet):
    queryset = CarImage.objects.all()
    serializer_class = CarImageSerializer
    parser_classes = [MultiPartParser, FormParser]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Получить список изображений машин",
        responses={200: CarImageSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Создать изображение машины",
        request_body=CarImageSerializer,
        responses={201: CarImageSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Получить изображение машины по ID",
        responses={200: CarImageSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Обновить изображение машины по ID",
        request_body=CarImageSerializer,
        responses={200: CarImageSerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Частично обновить изображение машины по ID",
        request_body=CarImageSerializer,
        responses={200: CarImageSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Удалить изображение машины по ID",
        responses={204: 'Изображение удалено'}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
