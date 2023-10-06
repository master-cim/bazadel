from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # Cтраница услуг
    path('service/', views.service, name='service'),
    # Страница со списком проектов
    path('project/', views.project_list),
    # Отдельная страница с информацией о проекте
    path('project/<slug:slug>/', views.project_detail),
]