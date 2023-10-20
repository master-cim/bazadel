from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # Cтраница услуг
    path('service/', views.service, name='service'),
    # Cтраница команды
    path('about/', views.about, name='about'),
    # Отдельная страница с информацией об услуге
    path('service/<slug:slug>/', views.project_detail),
    # Страница обучения
    path('learning/', views.learning, name='learning'),
    path('order/', views.OrderView.as_view(), name='form_order'),
]