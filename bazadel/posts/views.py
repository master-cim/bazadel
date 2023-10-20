from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import OrderForm


def index(request):
    template = 'posts/index.html'
    return render(request, template)


def service(request):
    template = 'posts/service.html'
    return render(request, template)


def about(request):
    template = 'posts/about.html'
    return render(request, template) 


def learning(request):
    template = 'posts/learning.html'
    return render(request, template) 


# Страница со списком проектов
def project_list(request):
    return HttpResponse('Список проектов')


# Страница с информацией об одном проекте;
# view-функция принимает параметр pk из path()
def project_detail(request, pk):
    return HttpResponse(f'Проект {pk}')

class OrderView(CreateView):  # Создаём свой класс, наследуем его от CreateView
    # C какой формой будет работать этот view-класс
    form_class = OrderForm    

    # Какой шаблон применить для отображения веб-формы
    template_name = 'includes/form_order.html'  

    # Куда переадресовать пользователя после того, как он отправит форму
    # success_url = '/thankyou/'
    success_url = reverse_lazy('posts:index')