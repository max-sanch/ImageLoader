from io import BytesIO

import requests
from PIL import Image
from django.core.files.base import ContentFile


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
    """Преобразование изображения в Django-файл"""
    f_object = BytesIO()
    image.save(f_object, format=format_img)
    return ContentFile(f_object.getvalue())
