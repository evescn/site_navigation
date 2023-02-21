# Generated by Django 3.2.5 on 2023-02-21 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_password_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='password',
            name='service_sid',
        ),
        migrations.AddField(
            model_name='service',
            name='password_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Password', to='app.password', verbose_name='账户'),
            preserve_default=False,
        ),
    ]