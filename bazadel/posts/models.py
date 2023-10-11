from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator


User = get_user_model()


class Service(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Order(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='serviсes', verbose_name='Заказчик услуги'
    )
    service = models.ForeignKey(
        'Service',
        on_delete=models.SET_NULL,
        related_name='types',
        null=True,
        verbose_name='Вид услуги',
        help_text='Выберите вид услуги'
    )
    text = models.TextField('Текст заявки',
                            help_text='Введите текст заявки')
    phone_regex = RegexValidator(regex=r'^\+?7?\d{10}$', message="Телефонный номер должен быть введен в формате: '+799999999'. Допускается не более 11 цифр.")
    phone_number = models.CharField(validators=[phone_regex], max_length=12, blank=False, null=False,)
    e_mail = models.EmailField(verbose_name='Электронный адрес',
                               max_length=200,
                               unique=True)
    pub_date = models.DateTimeField('Дата заявки',
                                    auto_now_add=True)
    

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text[:15]



    
