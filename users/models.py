from django.db import models
from django.contrib.auth.models import User


GENDER = (
    ('М', 'М'),
    ('Ж', 'Ж')
)
class CustomUser(User):
    class Meta:
        verbose_name = 'пользователя'
        verbose_name_plural = 'пользователи'
    phone_number = models.CharField(max_length=14, default='+996')
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=100, choices=GENDER)

    def __str__(self):
        return self.username