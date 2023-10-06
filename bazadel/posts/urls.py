from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница со списком проектов
    path('project/', views.project_list),
    # Отдельная страница с информацией о проекте
    path('project/<slug:slug>/', views.project_detail),
]