from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddImageView.as_view(), name='add_image'),
    path('detail/<int:pk>/', views.ImageDetailView.as_view(), name='one_image'),
    path('', views.HomePageView.as_view(), name='home_page'),
]
