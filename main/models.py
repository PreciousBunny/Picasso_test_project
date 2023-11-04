from django.db import models


# Create your models here.

class File(models.Model):
    """
    Класс описания модели File.
    """
    file = models.FileField(upload_to='file/', verbose_name='Файл')
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')
    processed = models.BooleanField(default=False, verbose_name='Статус обработки файла')

    class Meta:
        """
        Класс мета-настроек.
        """
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
        ordering = ('-uploaded_at',)
