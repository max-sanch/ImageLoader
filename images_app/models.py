import os.path
from django.db import models


class Image(models.Model):
    """Загруженные изображения"""
    file = models.ImageField(
        verbose_name="Изображение",
        blank=True,
        null=True,
        upload_to='images/',
        max_length=512
    )

    def filename(self):
        return os.path.basename(self.file.name)


class ImageSize(models.Model):
    """Размер изображения указанный пользователем"""
    image = models.OneToOneField(Image, on_delete=models.CASCADE)
    width = models.IntegerField(verbose_name="Ширина изображения")
    height = models.IntegerField(verbose_name="Высота изображения")
