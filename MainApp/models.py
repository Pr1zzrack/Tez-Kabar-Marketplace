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

# class Car(models.Model):
#     title = models.CharField(max_length=56, verbose_name='Название объявления')
#     year = models.IntegerField(verbose_name='Год')
#     mileage = models.IntegerField(verbose_name='Пробег (км.)')
#     model = models.CharField(max_length=70, verbose_name='Модель')
#     state = models.CharField(max_length=5, choices=[('б/у', 'Б/у'), ('новый', 'Новый')], verbose_name='Состояние')
#     fuel = ArrayField(models.CharField(max_length=14, choices=[('бензин', 'Бензин'), ('газ', 'Газ'), ('гибрид', 'Гибрид'), ('дизель', 'Дизель'), ('электромобиль', 'Электромобиль')], verbose_name='Топливо'), default=list)
#     kuzov = models.CharField(max_length=70, choices=[('бус', 'Бус'), ('внедорожник', 'Внедорожник'), ('кабриолет', 'Кабриолет'), ('кроссовер', 'Кроссовер'), ('купе', 'Купе'), ('лимузин', 'Лимузин'), ('минивэн', 'Минивэн'), ('пикап', 'Пикап'), ('седан', 'Седан'), ('универсал', 'Универсал'), ('фургон', 'Фургон'), ('хэтчбэк', 'Хэтчбэк')], verbose_name='Кузов')
#     transmission = ArrayField(models.CharField(max_length=9, choices=[('типтроник', 'Типтроник'), ('робот', 'Робот'), ('механика', 'Механика'), ('вариатор', 'Вариатор'), ('автомат', 'Автомат')], verbose_name='Коробка передач'), default=list)
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
#     technical_condition = ArrayField(models.CharField(max_length=14, choices=[('аварийное', 'Аварийное'), ('битый', 'Битый'), ('идеальное', 'Идеальное'), ('на запчасти', 'На запчасти'), ('хорошее', 'Хорошее')], verbose_name='Техническое состояние'), default=list)
#     customs_clearance = models.CharField(max_length=14, choices=[('не растаможен', 'Не растаможен'), ('растаможен', 'Растаможен')], verbose_name='Растаможка')
#     calculation = ArrayField(models.CharField(max_length=16, choices=[('возможен обмен', 'Возможен обмен'), ('кредит', 'Кредит'), ('обмена нет', 'Обмена нет'), ('оплата наличными', 'Оплата наличными'), ('рассрочка', 'Рассрочка')], verbose_name='Расчет'), default=list)
#     availability = models.CharField(max_length=14, choices=[('на заказ', 'На заказ'), ('в наличии', 'В наличии')], verbose_name='Наличие')
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     phone_numbers = ArrayField(models.CharField(max_length=13, default=list))
#     car_images = ArrayField(models.ImageField(default=list))

#     def __str__(self):
#         return self.title
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField

class Car(models.Model):
    title = models.CharField(max_length=56, verbose_name='Название объявления')
    year = models.IntegerField(verbose_name='Год')
    mileage = models.IntegerField(verbose_name='Пробег (км.)')
    model = models.CharField(max_length=70, verbose_name='Модель')
    state = models.CharField(max_length=5, choices=[('б/у', 'Б/у'), ('новый', 'Новый')], verbose_name='Состояние')
    fuel = models.JSONField(default=list, verbose_name='Топливо')
    kuzov = models.CharField(max_length=70, choices=[('бус', 'Бус'), ('внедорожник', 'Внедорожник'), ('кабриолет', 'Кабриолет'), ('кроссовер', 'Кроссовер'), ('купе', 'Купе'), ('лимузин', 'Лимузин'), ('минивэн', 'Минивэн'), ('пикап', 'Пикап'), ('седан', 'Седан'), ('универсал', 'Универсал'), ('фургон', 'Фургон'), ('хэтчбэк', 'Хэтчбэк')], verbose_name='Кузов')
    transmission = models.JSONField(default=list, verbose_name='Коробка передач')
    steering_wheel = models.CharField(max_length=6, choices=[('слева', 'Слева'), ('справа', 'Справа')], verbose_name='Руль')
    drive_unit = models.CharField(max_length=20, choices=[('4WD, полный', '4WD, полный'), ('AWD, полный', 'AWD, полный'), ('задний', 'Задний'), ('передний', 'Передний')], verbose_name='Привод')
    COLOR_CHOICES = [
        ('красный', 'Красный'),
        ('синий', 'Синий'),
        ('зелёный', 'Зелёный'),
        ('чёрный', 'Чёрный'),
        ('белый', 'Белый'),
        ('серебристый', 'Серебристый'),
        ('жёлтый', 'Жёлтый'),
    ]
    color = models.CharField(max_length=12, choices=COLOR_CHOICES, verbose_name='Цвет')
    ENGINE_VOLUME_CHOICES = [(str(i/10), str(i/10)) for i in range(1, 101)]
    engine_volume = models.CharField(max_length=4, choices=ENGINE_VOLUME_CHOICES, verbose_name='Объем двигателя')
    VIN_code = models.CharField(max_length=14, choices=[('с VIN кодом', 'С VIN кодом'), ('без VIN кода', 'Без VIN кода')], verbose_name='VIN код')
    technical_condition = models.JSONField(default=list, verbose_name='Техническое состояние')
    customs_clearance = models.CharField(max_length=14, choices=[('не растаможен', 'Не растаможен'), ('растаможен', 'Растаможен')], verbose_name='Растаможка')
    calculation = models.JSONField(default=list, verbose_name='Расчет')
    availability = models.CharField(max_length=14, choices=[('на заказ', 'На заказ'), ('в наличии', 'В наличии')], verbose_name='Наличие')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    phone_numbers = models.JSONField(default=list)
    car_images = models.JSONField(default=list)

    def __str__(self):
        return self.title
