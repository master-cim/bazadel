from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    template = 'posts/index.html'
    return render(request, template) 


# Страница со списком мороженого
def project_list(request):
    return HttpResponse('Список проектов')


# Страница с информацией об одном проекте;
# view-функция принимает параметр pk из path()
def project_detail(request, pk):
    return HttpResponse(f'Проект {pk}') 