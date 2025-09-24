from django.db import models

class Todo(models.Model):
  CHOICE_TYPE = (
    ('Выполнено', 'Выполнено'),
    ('Не выполнено', 'Не выполнено')
  )
  title = models.CharField(max_length=100, verbose_name='напишите задачу')
  choice_type = models.CharField(max_length=100, verbose_name='выберите вариант',
                           choices=CHOICE_TYPE)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'{self.title} - {self.choice_type}'
  
