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
    # path('service/<slug:slug>/', views.project_detail),
    # Страница обучения
    path('learning/', views.learning, name='learning'),
    path('website/', views.website, name='website'),
    path('database/', views.database, name='database'),
    path('telega/', views.telega, name='telega'),
    path('prom/', views.promotion, name='promotion'),
    path('analys/', views.analys, name='analys'),
    path('learning/eduweb', views.eduweb, name='eduweb'),
    path('learning/edudb', views.edudb, name='edudb'),
    path('learning/edutel', views.edutel, name='edutel'),
]
