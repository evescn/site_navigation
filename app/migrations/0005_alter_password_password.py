# Generated by Django 3.2.5 on 2023-02-20 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20230220_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='password',
            name='password',
            field=models.CharField(default='', max_length=100, verbose_name='用户密码'),
        ),
    ]