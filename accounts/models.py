from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, verbose_name="Телефон")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    education = models.CharField(max_length=100, verbose_name="Образование")
    experience = models.TextField(verbose_name="Опыт работы")
    skills = models.TextField(verbose_name="Навыки")
    desired_position = models.CharField(max_length=100, verbose_name="Желаемая должность")
    resume = models.FileField(upload_to='resumes/', null=True, blank=True, verbose_name="Резюме")
    linkedin = models.URLField(blank=True, null=True, verbose_name="LinkedIn")
    portfolio = models.URLField(blank=True, null=True, verbose_name="Портфолио")

    def __str__(self):
        return self.username
