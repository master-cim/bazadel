from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db.models import Q, F


User = get_user_model()


class Service(models.Model):
    title = models.CharField(max_length=200,)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Status(models.Model):
    PREPARATION = 'INITIAL'
    SPECIFICATION = 'TZ'
    PROJECT = 'PROJECT'
    DESIGN = 'DESIGN'
    DEVELOPING = 'DEVELOP'
    TESTING = 'TEST'
    STARTUP = 'STARTUP'
    MAINTAIN ='MAINTAIN'
    WAIT = 'WAIT'
    START = 'START'
    FINISH = 'FINISH'
 
    STATUS_TYPES = (
        (WAIT, 'Ожидание'),
        (START, 'Старт'),
        (PREPARATION, 'Интервью'),
        (SPECIFICATION, 'Техническое задание'),
        (PROJECT, 'Проект'),
        (DESIGN, 'Дезайн'),
        (DEVELOPING, 'Разработка'),
        (TESTING, 'Тестирование'),
        (STARTUP, 'Запуск продукта'),
        (MAINTAIN, 'Техническая поддержка'),
        (FINISH, 'Проект закрыт')
    )
    
    name = models.CharField(max_length=21, choices=STATUS_TYPES)
    description = models.TextField()
    prev_status = models.ForeignKey('self', null=True, blank=True, related_name='status', on_delete = models.SET_NULL, )
    

    def __str__(self):
        return self.name


class Order(models.Model):
    author = models.CharField('Имя', max_length=100,
                              )
    service = models.ForeignKey(
        'Service',
        on_delete=models.SET_NULL,
        related_name='types',
        null=True, blank=True,
        verbose_name='Выберите вид услуги',
    )
    text = models.TextField('Текст заявки',)
    phone_regex = RegexValidator(regex=r'^\+?7?\d{10}$', message="Телефонный номер должен быть введен в формате: '+799999999'. Допускается не более 11 цифр.")
    phone_number = models.CharField(verbose_name='Телефон', validators=[phone_regex], max_length=12,)
    e_mail = models.EmailField(verbose_name='Электронный адрес',
                               max_length=200,
                               )
    pub_date = models.DateTimeField('Дата заявки',
                                    auto_now_add=True)
    

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.author + " " + self.text[:15]



    
class Project(models.Model):
    title = models.CharField(max_length=250)
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='project', verbose_name='Заказчик услуги'
    )
    order = models.ForeignKey('Order', on_delete=models.CASCADE,
                              related_name='order', verbose_name='Заказ', 
                              help_text='Выберите заказ', null=True, blank=True,)
    status = models.ManyToManyField(Status, through="Workflow")
    project_mng = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='project_mng',
                               null=True, blank=True,)
    start_date = models.DateTimeField('Дата заявки',
                                    auto_now_add=True)
    

    class Meta:
        ordering = ('-start_date',)

    def __str__(self):
        return self.title[:15]


class Workflow(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    start_date = models.DateTimeField('Дата начала этапа',
                                    auto_now_add=True)
    end_date = models.DateTimeField('Дата окончания этапа',
                                    null=True,
                               blank=True,)
    process_mng = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='process_mng',
                               null=True,
                               blank=True,)
    
    class Meta:
        ordering = ('-project',)
        constraints = [
            models.CheckConstraint(
                name='start_date_before_end_date',
                check=Q(start_date__lt=F('end_date'))
            )
        ]