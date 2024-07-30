from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'parent', 'category_icon', 'subcategories']

    def get_subcategories(self, obj):
        if obj.subcategories.exists():
            return CategorySerializer(obj.subcategories.all(), many=True).data
        return []


from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate

class MarkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marka
        fields = '__all__'

class BodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Body
        fields = '__all__'

class BodyColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyColor
        fields = '__all__'

class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = '__all__'

class CheckpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkpoint
        fields = '__all__'

class DriveUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriveUnit
        fields = '__all__'

class StreengWhellSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreengWhell
        fields = '__all__'

class CarImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = CarImage
        fields = ['id', 'car', 'image', 'image_url']
        extra_kwargs = {
            'image': {'write_only': True},
        }

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None

class CarReadSerializer(serializers.ModelSerializer):
    marka_name = serializers.SerializerMethodField()
    year_of_manufacture_name = serializers.SerializerMethodField()
    body_name = serializers.SerializerMethodField()
    body_color_name = serializers.SerializerMethodField()
    checkpoint_name = serializers.SerializerMethodField()
    drive_unit_name = serializers.SerializerMethodField()
    steering_wheel_name = serializers.SerializerMethodField()
    images = CarImageSerializer(many=True, read_only=True)

    class Meta:
        model = Car
        fields = [
            'id', 'marka_name', 'year_of_manufacture_name', 'body_name', 
            'car_model', 'price', 'engine', 'power', 'owners', 'body_color_name', 'name', 
            'mileage', 'phone_number', 'checkpoint_name', 'drive_unit_name', 'steering_wheel_name',
            'images'
        ]

    def get_marka_name(self, obj):
        return obj.marka.marka if obj.marka else None

    def get_year_of_manufacture_name(self, obj):
        return obj.year_of_manufacture.year_of_manufacture if obj.year_of_manufacture else None

    def get_body_name(self, obj):
        return obj.body.body if obj.body else None

    def get_body_color_name(self, obj):
        return obj.body_color.body_color if obj.body_color else None

    def get_checkpoint_name(self, obj):
        return obj.checkpoint.checkpoint if obj.checkpoint else None

    def get_drive_unit_name(self, obj):
        return obj.drive_unit.drive_unit if obj.drive_unit else None

    def get_steering_wheel_name(self, obj):
        return obj.steering_wheel.steering_wheel if obj.steering_wheel else None

class CarWriteSerializer(serializers.ModelSerializer):
    image_uploads = serializers.ListField(
        child=serializers.ImageField(write_only=True),
        write_only=True,
        required=False
    )

    class Meta:
        model = Car
        fields = [
            'marka', 'car_model', 'price', 'year_of_manufacture', 
            'mileage', 'body', 'body_color', 'engine', 'power', 'name', 'phone_number',
            'checkpoint', 'drive_unit', 'owners', 'steering_wheel', 'image_uploads'
        ]

    def create(self, validated_data):
        image_uploads = validated_data.pop('image_uploads', [])
        car = Car.objects.create(**validated_data)
        for image in image_uploads:
            CarImage.objects.create(car=car, image=image)
        return car

    def update(self, instance, validated_data):
        image_uploads = validated_data.pop('image_uploads', [])
        instance = super().update(instance, validated_data)
        for image in image_uploads:
            CarImage.objects.create(car=instance, image=image)
        return instance
