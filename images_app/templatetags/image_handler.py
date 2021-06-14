from django import template
from django.shortcuts import get_object_or_404

from images_app import models

register = template.Library()


@register.simple_tag()
def get_image_url(image_id):
    image = get_object_or_404(models.Image, id=int(image_id))
    try:
        image_sized = models.ImageSize.objects.get(image=image)
        return image_sized.file.url
    except models.ImageSize.DoesNotExist:
        return image.file.url
