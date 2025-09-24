from django.db import models

class Driver(models.Model):
  name = models.CharField(max_length=10, verbose_name='как вас зовут?')
  license_number = models.CharField(max_length=10 , default='0KG', verbose_name='введите номер машины')

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = 'Хозяина'
    verbose_name_plural = 'Хозяйева'
  

class Car(models.Model):
  driver = models.OneToOneField(Driver, on_delete=models.CASCADE, related_name='driver')
  brand = models.CharField(max_length=100, verbose_name='введите номер машины')
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'{self.driver} - {self.brand}'
  
  class Meta:
    verbose_name = 'Машину'
    verbose_name_plural = 'Машины'