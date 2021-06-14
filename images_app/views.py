from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404

from .models import Image
from .forms import AddImageForms, ImageDetailForms


class HomePageView(ListView):
    """Главная страница со списком изображений"""
    template_name = 'home_page.html'
    model = Image


class AddImageView(FormView):
    """Добавление изображения двумя способами (ссылка или файл)"""
    template_name = 'add_image.html'
    form_class = AddImageForms
    success_url = None

    def form_valid(self, form):
        image = form.save()
        self.success_url = reverse_lazy('one_image', kwargs={'pk': image.pk})
        return super().form_valid(form)


class ImageDetailView(FormView):
    """Просмотр изображения с возможностью изменить размер"""
    template_name = 'one_image.html'
    form_class = ImageDetailForms
    success_url = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image'] = get_object_or_404(Image, id=self.kwargs.get('pk'))
        return context

    def get_success_url(self):
        return reverse_lazy('one_image', kwargs={'pk': self.kwargs.get('pk')})
