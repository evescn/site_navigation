# Generated by Django 3.2.5 on 2023-02-21 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20230221_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='password',
            name='password',
            field=models.CharField(blank='', default='', max_length=100, verbose_name='用户密码'),
        ),
    ]