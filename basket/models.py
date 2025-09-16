# basket/models.py
from django.db import models

# Модель для дополнительного задания
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

# Основная модель заказа
class Order(models.Model):
    # Статусы заказа
    STATUS_CHOICES = [
        ('выполнено', 'Выполнено'),
        ('не выполнено', 'Не выполнено'),
    ]

    # Поля для заказа
    name = models.CharField('Имя клиента', max_length=100)
    phone_number = models.CharField('Номер телефона', max_length=20)
    card_number = models.CharField('Номер карты', max_length=16)
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='не выполнено')
    created_at = models.DateTimeField(auto_now_add=True)

    # Связь с книгой (для дополнительного задания)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')

    def __str__(self):
        return f'Заказ {self.id} от {self.name}'