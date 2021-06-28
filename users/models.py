from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField('Email адрес', blank=True)
    phone = models.CharField('Номер телефона', max_length=30, blank=True)
        
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.username} {self.first_name} {self.last_name}'