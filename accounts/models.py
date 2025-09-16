from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Поля, унаследованные от AbstractUser:
    # username, password, email, first_name, last_name, is_staff, is_active, date_joined

    # 10 дополнительных полей для приёма на работу
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="Номер телефона")
    date_of_birth = models.DateField(blank=True, null=True, verbose_name="Дата рождения")
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name="Адрес проживания")
    education = models.CharField(max_length=100, blank=True, null=True, verbose_name="Образование")
    major = models.CharField(max_length=100, blank=True, null=True, verbose_name="Специальность")
    work_experience = models.TextField(blank=True, null=True, verbose_name="Опыт работы")
    desired_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Желаемая зарплата")
    skills = models.TextField(blank=True, null=True, verbose_name="Навыки")
    portfolio_url = models.URLField(max_length=200, blank=True, null=True, verbose_name="Ссылка на портфолио")
    linkedin_url = models.URLField(max_length=200, blank=True, null=True, verbose_name="Профиль LinkedIn")
    
    # Чтобы использовать эту модель, нужно настроить AUTH_USER_MODEL в settings.py
    def __str__(self):
        return self.username
    
    pass