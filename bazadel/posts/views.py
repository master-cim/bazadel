from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import OrderForm
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings



def index(request):
    template = 'posts/index.html'
    form = OrderForm(request.POST or None)
    if form.is_valid():
        subject = "Заявка от пользователя сайта"
        body = {
                'author': form.cleaned_data['author'],
                'phone_number': form.cleaned_data['phone_number'],
                'e_mail': form.cleaned_data['e_mail'],
                'text': form.cleaned_data['text'],
            }
        message = "\n".join(body.values())
        try:
            send_mail(subject, message, 
                          settings.EMAIL_HOST_USER,
                          ['basedeal@yandex.ru'])
        except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
        form = form.save(commit=False)
        form.save()
        return HttpResponseRedirect(reverse_lazy('posts:service'))

    context = {
        # ...,
        'form': form,
    }
    return render(request, template, context)


def service(request):
    template = 'posts/service.html'
    return render(request, template)


def about(request):
    template = 'posts/about.html'
    return render(request, template) 


def learning(request):
    template = 'posts/learning.html'
    return render(request, template)


def website(request):
    template = 'posts/website.html'
    form = OrderForm(request.POST or None)
    if form.is_valid():
        subject = "Заявка от пользователя сайта"
        body = {
                'author': form.cleaned_data['author'],
                'phone_number': form.cleaned_data['phone_number'],
                'e_mail': form.cleaned_data['e_mail'],
                'text': form.cleaned_data['text'],
            }
        message = "\n".join(body.values())
        try:
            send_mail(subject, message, 
                          settings.EMAIL_HOST_USER,
                          ['basedeal@yandex.ru'])
        except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
        form = form.save(commit=False)
        form.save()
        return HttpResponseRedirect(reverse_lazy('posts:service'))

    context = {
        # ...,
        'form': form,
    }
    return render(request, template, context)


# Страница со списком проектов
def project_list(request):
    return HttpResponse('Список проектов')


# Страница с информацией об одном проекте;
# view-функция принимает параметр pk из path()
# def project_detail(request, pk):
#     return HttpResponse(f'Проект {pk}')

def database(request):
    template = 'posts/database.html'
    form = OrderForm(request.POST or None)
    if form.is_valid():
        subject = "Заявка от пользователя сайта"
        body = {
                'author': form.cleaned_data['author'],
                'phone_number': form.cleaned_data['phone_number'],
                'e_mail': form.cleaned_data['e_mail'],
                'text': form.cleaned_data['text'],
            }
        message = "\n".join(body.values())
        try:
            send_mail(subject, message, 
                          settings.EMAIL_HOST_USER,
                          ['basedeal@yandex.ru'])
        except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
        form = form.save(commit=False)
        form.save()
        return HttpResponseRedirect(reverse_lazy('posts:service'))

    context = {
        # ...,
        'form': form,
    }
    return render(request, template, context)


def telega(request):
    template = 'posts/telega.html'
    form = OrderForm(request.POST or None)
    if form.is_valid():
        subject = "Заявка от пользователя сайта"
        body = {
                'author': form.cleaned_data['author'],
                'phone_number': form.cleaned_data['phone_number'],
                'e_mail': form.cleaned_data['e_mail'],
                'text': form.cleaned_data['text'],
            }
        message = "\n".join(body.values())
        try:
            send_mail(subject, message, 
                          settings.EMAIL_HOST_USER,
                          ['basedeal@yandex.ru'])
        except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
        form = form.save(commit=False)
        form.save()
        return HttpResponseRedirect(reverse_lazy('posts:service'))

    context = {
        # ...,
        'form': form,
    }
    return render(request, template, context)


def promotion(request):
    template = 'posts/promotion.html'
    form = OrderForm(request.POST or None)
    if form.is_valid():
        subject = "Заявка от пользователя сайта"
        body = {
                'author': form.cleaned_data['author'],
                'phone_number': form.cleaned_data['phone_number'],
                'e_mail': form.cleaned_data['e_mail'],
                'text': form.cleaned_data['text'],
            }
        message = "\n".join(body.values())
        try:
            send_mail(subject, message, 
                          settings.EMAIL_HOST_USER,
                          ['basedeal@yandex.ru'])
        except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
        form = form.save(commit=False)
        form.save()
        return HttpResponseRedirect(reverse_lazy('posts:service'))

    context = {
        # ...,
        'form': form,
    }
    return render(request, template, context)


def analys(request):
    template = 'posts/analys.html'
    form = OrderForm(request.POST or None)
    if form.is_valid():
        subject = "Заявка от пользователя сайта"
        body = {
                'author': form.cleaned_data['author'],
                'phone_number': form.cleaned_data['phone_number'],
                'e_mail': form.cleaned_data['e_mail'],
                'text': form.cleaned_data['text'],
            }
        message = "\n".join(body.values())
        try:
            send_mail(subject, message, 
                          settings.EMAIL_HOST_USER,
                          ['basedeal@yandex.ru'])
        except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
        form = form.save(commit=False)
        form.save()
        return HttpResponseRedirect(reverse_lazy('posts:service'))

    context = {
        # ...,
        'form': form,
    }
    return render(request, template, context)


def eduweb(request):
    template = 'posts/edu_web.html'
    form = OrderForm(request.POST or None)
    if form.is_valid():
        subject = "Заявка от пользователя сайта"
        body = {
                'author': form.cleaned_data['author'],
                'phone_number': form.cleaned_data['phone_number'],
                'e_mail': form.cleaned_data['e_mail'],
                'text': form.cleaned_data['text'],
            }
        message = "\n".join(body.values())
        try:
            send_mail(subject, message, 
                          settings.EMAIL_HOST_USER,
                          ['basedeal@yandex.ru'])
        except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
        form = form.save(commit=False)
        form.save()
        return HttpResponseRedirect(reverse_lazy('posts:learning'))

    context = {
        # ...,
        'form': form,
    }
    return render(request, template, context)


def edudb(request):
    template = 'posts/edu_db.html'
    form = OrderForm(request.POST or None)
    if form.is_valid():
        subject = "Заявка от пользователя сайта"
        body = {
                'author': form.cleaned_data['author'],
                'phone_number': form.cleaned_data['phone_number'],
                'e_mail': form.cleaned_data['e_mail'],
                'text': form.cleaned_data['text'],
            }
        message = "\n".join(body.values())
        try:
            send_mail(subject, message, 
                          settings.EMAIL_HOST_USER,
                          ['basedeal@yandex.ru'])
        except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
        form = form.save(commit=False)
        form.save()
        return HttpResponseRedirect(reverse_lazy('posts:learning'))

    context = {
        # ...,
        'form': form,
    }
    return render(request, template, context)


def edutel(request):
    template = 'posts/edu_tel.html'
    form = OrderForm(request.POST or None)
    if form.is_valid():
        subject = "Заявка от пользователя сайта"
        body = {
                'author': form.cleaned_data['author'],
                'phone_number': form.cleaned_data['phone_number'],
                'e_mail': form.cleaned_data['e_mail'],
                'text': form.cleaned_data['text'],
            }
        message = "\n".join(body.values())
        try:
            send_mail(subject, message, 
                          settings.EMAIL_HOST_USER,
                          ['basedeal@yandex.ru'])
        except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
        form = form.save(commit=False)
        form.save()
        return HttpResponseRedirect(reverse_lazy('posts:learning'))

    context = {
        # ...,
        'form': form,
    }
    return render(request, template, context)