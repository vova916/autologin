import django
from django.db import models
from django.contrib.auth.models import User

#Встановлення цін, вмістимості, особливостей кімнат/місць.

class Room(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    capacity = models.IntegerField(verbose_name="Місткість")
    features = models.TextField(verbose_name="Особливості")
    description = models.TextField(null=True, blank=True, verbose_name="Опис")
    image = models.ImageField(upload_to='room_images/', null=True, blank=True, verbose_name="Зображення")
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Категорія", related_name="rooms")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Кімната"
        verbose_name_plural = "Кімнати"
        
        ordering = ['name']
    
class Booking(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name="Кімната", related_name="bookings")
    check_in = models.DateField(verbose_name="Дата заїзду")
    check_out = models.DateField(verbose_name="Дата виїзду")
    customer = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Клієнт", related_name="bookings")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    
    def __str__(self):
        return f"{self.customer} - {self.room.name} ({self.check_in} to {self.check_out})"
    
    class Meta:
        ordering = ['-date_created']
        verbose_name = "Бронювання"
        verbose_name_plural = "Бронювання"


class User(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Телефон")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Клієнт"
        verbose_name_plural = "Клієнти"
    
    
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"