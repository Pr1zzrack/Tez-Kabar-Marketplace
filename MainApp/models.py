from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.postgres.fields import ArrayField


class CustomUser(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subcategories', null=True, blank=True)
    category_icon = models.ImageField(upload_to='category_icon/')

    def __str__(self):
        return self.name






class Marka(models.Model):
    marka = models.CharField(max_length=40, verbose_name='Марка')

    def __str__(self) -> str:
        return f'{self.marka}'

class Body(models.Model):
    body = models.CharField(max_length=42, verbose_name='Тип кузова')

    def __str__(self) -> str:
        return f'{self.body}'

class BodyColor(models.Model):
    body_color = models.CharField(max_length=32, verbose_name='Цвет кузова')

    def __str__(self) -> str:
        return f'{self.body_color}'

class Year(models.Model):
    year_of_manufacture = models.PositiveIntegerField(default=2020, verbose_name='Год выпуска')

    def __str__(self) -> str:
        return f'{self.year_of_manufacture}'

class Checkpoint(models.Model):
    checkpoint = models.CharField(max_length=120, verbose_name='Коробка передач')

    def __str__(self) -> str:
        return f'{self.checkpoint}'

class DriveUnit(models.Model):
    drive_unit = models.CharField(max_length=42, verbose_name='Привод')

    def __str__(self) -> str:
        return f'{self.drive_unit}'

class StreengWhell(models.Model):
    steering_wheel = models.CharField(max_length=10, verbose_name='Руль')

    def __str__(self) -> str:
        return f'{self.steering_wheel}'

class Car(models.Model):
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE, verbose_name='Марка')
    car_model = models.CharField(max_length=75, verbose_name='Модель')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')
    year_of_manufacture = models.ForeignKey(Year, on_delete=models.CASCADE, verbose_name='Год')
    mileage = models.PositiveIntegerField(default=0, verbose_name='Пробег')
    body = models.ForeignKey(Body, on_delete=models.CASCADE, verbose_name='Кузов')
    body_color = models.ForeignKey(BodyColor, on_delete=models.CASCADE, verbose_name='Цвет кузова')
    engine = models.CharField(max_length=50, verbose_name='Двигатель')
    power = models.CharField(max_length=142, verbose_name='Мощность')
    checkpoint = models.ForeignKey(Checkpoint, on_delete=models.CASCADE, verbose_name='Коробка передач')
    drive_unit = models.ForeignKey(DriveUnit, on_delete=models.CASCADE, verbose_name='Привод')
    owners = models.PositiveSmallIntegerField(default=1, blank=True, null=True, verbose_name='Количество владельцев')
    steering_wheel = models.ForeignKey(StreengWhell, on_delete=models.CASCADE, verbose_name='Руль')
    name = models.CharField(max_length=42, verbose_name='Имя')
    phone_number = models.CharField(max_length=15, verbose_name='Номер продавца')

    def __str__(self):
        return f'{self.marka} - {self.year_of_manufacture}'

class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='images', verbose_name='id машины')
    image = models.ImageField(upload_to='car_images/', verbose_name='Фото машины')

    def __str__(self) -> str:
        return f'{self.car.id} - {self.image.url}'





# class State(models.Model):
#     state = models.CharField(max_length=7, verbose_name='Состояние')

#     def __str__(self) -> str:
#         return self.state

# class Kuzov(models.Model):
#     kuzov = models.CharField(max_length=70, verbose_name='Кузов')

#     def __str__(self) -> str:
#         return self.kuzov

# class SteeringWheel(models.Model):
#     steering_wheel = models.CharField(max_length=6, verbose_name='Руль')

#     def __str__(self) -> str:
#         return self.steering_wheel

# class DriveUnit(models.Model):
#     drive_unit = models.CharField(max_length=20, verbose_name='Привод')

#     def __str__(self) -> str:
#         return self.drive_unit

# class Color(models.Model):
#     color = models.CharField(max_length=12, verbose_name='Цвет')

#     def __str__(self) -> str:
#         return self.color

# class EngineVolume(models.Model):
#     engine_volume = models.CharField(max_length=4, verbose_name='Объем двигателя')

#     def __str__(self) -> str:
#         return self.engine_volume

# # class VINCode(models.Model):
# #     VIN_code = models.CharField(max_length=14, verbose_name='VIN код')

# #     def __str__(self) -> str:
# #         return self.VIN_code

# class CustomsClearance(models.Model):
#     customs_clearance = models.CharField(max_length=14, verbose_name='Растаможка')

#     def __str__(self) -> str:
#         return self.customs_clearance

# class Availability(models.Model):
#     availability = models.CharField(max_length=14, verbose_name='Наличие')

#     def __str__(self) -> str:
#         return self.availability

# class Transmission(models.Model):
#     transmission = models.CharField(max_length=9, verbose_name='Коробка передач')

#     def __str__(self) -> str:
#         return self.transmission

# class TechnicalCondition(models.Model):
#     technical_condition = models.CharField(max_length=14, verbose_name='Техническое состояние')

#     def __str__(self) -> str:
#         return self.technical_condition

# class Calculation(models.Model):
#     calculation = models.CharField(max_length=16, verbose_name='Расчет')

#     def __str__(self) -> str:
#         return self.calculation

# # class PhoneNumber(models.Model):
# #     phone_number = models.CharField(max_length=13)

# #     def __str__(self) -> str:
# #         return self.phone_number

# class CarImage(models.Model):
#     car_image = models.ImageField()

#     def __str__(self) -> str:
#         return self.car_image

# class Fuel(models.Model):
#     fuel = models.CharField(max_length=14, verbose_name='Топливо')

#     def __str__(self) -> str:
#         return self.fuel

# class Car(models.Model):
#     title = models.CharField(max_length=56, verbose_name='Название объявления')
#     year = models.IntegerField(verbose_name='Год')
#     mileage = models.IntegerField(verbose_name='Пробег (км.)')
#     model = models.CharField(max_length=70, verbose_name='Модель')
#     state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name='Состояние')
#     kuzov = models.ForeignKey(Kuzov, on_delete=models.CASCADE, verbose_name='Кузов')
#     steering_wheel = models.ForeignKey(SteeringWheel, on_delete=models.CASCADE, verbose_name='Руль')
#     drive_unit = models.ForeignKey(DriveUnit, on_delete=models.CASCADE, verbose_name='Привод')
#     color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name='Цвет')
#     engine_volume = models.ForeignKey(EngineVolume, on_delete=models.CASCADE, verbose_name='Объем двигателя')
#     # VIN_code = models.ForeignKey(VINCode, on_delete=models.CASCADE, verbose_name='VIN код')
#     VIN_code = models.CharField(max_length=14, verbose_name='VIN код')
#     customs_clearance = models.ForeignKey(CustomsClearance, on_delete=models.CASCADE, verbose_name='Растаможка')
#     availability = models.ForeignKey(Availability, on_delete=models.CASCADE, verbose_name='Наличие')
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     # далжны быть списком и принемать несколько варинатов
#     transmission = models.ForeignKey(Transmission, on_delete=models.CASCADE, verbose_name='Коробка передач')
#     technical_condition = models.ForeignKey(TechnicalCondition, on_delete=models.CASCADE, verbose_name='Техническое состояние')
#     calculation = models.ForeignKey(Calculation, on_delete=models.CASCADE, verbose_name='Расчет')
#     # phone_number = models.ForeignKey(PhoneNumber, on_delete=models.CASCADE)
#     phone_number = models.CharField(max_length=13)
#     car_image = models.ForeignKey(CarImage, on_delete=models.CASCADE)
#     fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title

# from django.db import models
# from django.contrib.postgres.fields import ArrayField
# from django.contrib.postgres.fields import JSONField

# class Car(models.Model):
#     title = models.CharField(max_length=56, verbose_name='Название объявления')
#     year = models.IntegerField(verbose_name='Год')
#     mileage = models.IntegerField(verbose_name='Пробег (км.)')
#     model = models.CharField(max_length=70, verbose_name='Модель')
#     state = models.CharField(max_length=5, choices=[('б/у', 'Б/у'), ('новый', 'Новый')], verbose_name='Состояние')
#     fuel = models.JSONField(default=list, verbose_name='Топливо')
#     kuzov = models.CharField(max_length=70, choices=[('бус', 'Бус'), ('внедорожник', 'Внедорожник'), ('кабриолет', 'Кабриолет'), ('кроссовер', 'Кроссовер'), ('купе', 'Купе'), ('лимузин', 'Лимузин'), ('минивэн', 'Минивэн'), ('пикап', 'Пикап'), ('седан', 'Седан'), ('универсал', 'Универсал'), ('фургон', 'Фургон'), ('хэтчбэк', 'Хэтчбэк')], verbose_name='Кузов')
#     transmission = models.JSONField(default=list, verbose_name='Коробка передач')
#     steering_wheel = models.CharField(max_length=6, choices=[('слева', 'Слева'), ('справа', 'Справа')], verbose_name='Руль')
#     drive_unit = models.CharField(max_length=20, choices=[('4WD, полный', '4WD, полный'), ('AWD, полный', 'AWD, полный'), ('задний', 'Задний'), ('передний', 'Передний')], verbose_name='Привод')
#     COLOR_CHOICES = [
#         ('красный', 'Красный'),
#         ('синий', 'Синий'),
#         ('зелёный', 'Зелёный'),
#         ('чёрный', 'Чёрный'),
#         ('белый', 'Белый'),
#         ('серебристый', 'Серебристый'),
#         ('жёлтый', 'Жёлтый'),
#     ]
#     color = models.CharField(max_length=12, choices=COLOR_CHOICES, verbose_name='Цвет')
#     ENGINE_VOLUME_CHOICES = [(str(i/10), str(i/10)) for i in range(1, 101)]
#     engine_volume = models.CharField(max_length=4, choices=ENGINE_VOLUME_CHOICES, verbose_name='Объем двигателя')
#     VIN_code = models.CharField(max_length=14, choices=[('с VIN кодом', 'С VIN кодом'), ('без VIN кода', 'Без VIN кода')], verbose_name='VIN код')
#     technical_condition = models.JSONField(default=list, verbose_name='Техническое состояние')
#     customs_clearance = models.CharField(max_length=14, choices=[('не растаможен', 'Не растаможен'), ('растаможен', 'Растаможен')], verbose_name='Растаможка')
#     calculation = models.JSONField(default=list, verbose_name='Расчет')
#     availability = models.CharField(max_length=14, choices=[('на заказ', 'На заказ'), ('в наличии', 'В наличии')], verbose_name='Наличие')
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     phone_numbers = models.JSONField(default=list)
#     car_images = models.JSONField(default=list)

#     def __str__(self):
#         return self.title
