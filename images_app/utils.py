from io import BytesIO

import requests
from PIL import Image
from django.core.files.base import ContentFile
from django.shortcuts import get_object_or_404

from . import models


def get_image_to_url(url):
    """Получение изображения по ссылки"""
    try:
        request = requests.get(url)
        image = Image.open(BytesIO(request.content))
        return image
    except Exception:
        return None


def get_url_tail(url, format_img):
    """Получение названия файла из ссылки"""
    name = url.split('/')[-1]
    if name.split('.')[-1] != format_img.lower():
        name += '.%s' % format_img.lower()
    return name


def pil_to_django(image, format_img):
    """Преобразование изображения в файл Django"""
    f_object = BytesIO()
    image.save(f_object, format=format_img)
    return ContentFile(f_object.getvalue())


def sizing_image(image_id, width, height):
    """Изменение размера изображения"""
    image = get_object_or_404(models.Image, id=image_id)
    image_pil = Image.open(image.file.path)
    image_format = image_pil.format

    if width and not height:
        w_percent = (float(width) / float(image_pil.size[0]))
        height = int((float(image_pil.size[1]) * float(w_percent)))

    elif not width and height:
        h_percent = (float(height) / float(image_pil.size[1]))
        width = int((float(image_pil.size[0]) * float(h_percent)))

    image_pil = image_pil.resize((int(width), int(height)), Image.ANTIALIAS)
    django_image = pil_to_django(image_pil, image_format)
    image_sized, created = models.ImageSize.objects.update_or_create(
        image=image, defaults={'width': int(width), 'height': int(height)}
    )
    image_sized.file.save(image.filename(), django_image)
    return image_sized
