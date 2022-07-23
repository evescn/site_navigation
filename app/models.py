from django.db import models


# Create your models here.
# python manage.py makemigrations
# python manage.py migrate

class Env(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)


class Service(models.Model):
    sid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    url = models.CharField(max_length=500)
    env_id = models.ForeignKey(to="Env", to_field='id', on_delete=models.CASCADE)
    password_id = models.ForeignKey(to="Password", to_field='id', on_delete=models.CASCADE)


class Password(models.Model):
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    # b = models.ForeignKey(to="Service", to_field='sid', on_delete=models.CASCADE)
