from django.db import models
from django.urls import reverse


class User(models.Model):
    """Типичный класс модели, производный от класса Model."""

    # Поля
    username = models.CharField(max_length=30, help_text='никнейм')
    firstname = models.CharField(max_length=20, help_text='Имя')
    lastname = models.CharField(max_length=30, help_text='Фамилия')
    email = models.CharField(max_length=70, help_text='Email')
    password1 = models.CharField(max_length=30, help_text='Пароль')
    password2 = models.CharField(max_length=30, help_text='Повторите пароль')

    def __str__(self):
        """Строка для представления объекта MyModelName (например, в административной панели и т.д.)."""
        return self.username
