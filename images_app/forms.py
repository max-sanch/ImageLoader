from django import forms
from django.core.exceptions import ValidationError

from .models import Image
from . import utils


class AddImageForms(forms.Form):
    """Форма добавления изображения"""
    url = forms.URLField(label='Ссылка', required=False)
    file = forms.ImageField(label='Файл', required=False, max_length=512)

    def clean(self):
        url = self.data.get("url")
        file = self.cleaned_data.get("file")

        if url and file:
            raise ValidationError(
                "Введено два варианта загрузки изображения"
            )

        if not url and not file:
            raise ValidationError(
                "Не введено ни одного варианта загрузки изображения"
            )

    def clean_url(self):
        url = self.cleaned_data.get("url")
        if url:
            image = utils.get_image_to_url(url)
            if image is None:
                raise ValidationError(
                    "Недействительное изображение. Ошибка загрузки изображения."
                )
            self.loaded_image = image
        return url

    def save(self, commit=True):
        if len(self.files.getlist('file')) != 0:
            image = Image(
                file=self.files.getlist('file')[0]
            )
        else:
            filename = utils.get_url_tail(self.cleaned_data.get('url'), self.loaded_image.format)
            django_image = utils.pil_to_django(self.loaded_image, self.loaded_image.format)
            image = Image()
            image.file.save(filename, django_image)

        if commit:
            image.save()
        return image


class ImageDetailForms(forms.Form):
    """Форма изменения размера изображения"""
    width = forms.IntegerField(label='Ширина', min_value=1, required=False)
    height = forms.IntegerField(label='Высота', min_value=1, required=False)
