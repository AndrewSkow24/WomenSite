from django.db import models

# Create your models here.
class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    # auto_now_add - позволяет фиксировать текущее время только в момент первого добавления записи в таблицу БД
    time_create = models.DateTimeField(auto_now_add=True)
    # фиксирует текущее время всякий раз при изменении или добавлении записи в таблицу БД
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)