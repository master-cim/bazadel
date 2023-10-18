# Generated by Django 4.2.5 on 2023-10-18 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0004_alter_status_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='service',
            field=models.ForeignKey(blank=True, help_text='Выберите вид услуги', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='types', to='posts.service', verbose_name='Вид услуги'),
        ),
        migrations.AlterField(
            model_name='project',
            name='order',
            field=models.ForeignKey(blank=True, help_text='Выберите заказ', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='posts.order', verbose_name='Заказ'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_mng',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_mng', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='workflow',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания этапа'),
        ),
        migrations.AlterField(
            model_name='workflow',
            name='process_mng',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='process_mng', to=settings.AUTH_USER_MODEL),
        ),
    ]
