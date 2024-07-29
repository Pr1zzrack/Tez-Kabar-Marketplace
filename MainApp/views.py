from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .models import *
from .serializers import *


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'
    parser_classes = [MultiPartParser, FormParser]

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'id'
    parser_classes = [MultiPartParser, FormParser]

