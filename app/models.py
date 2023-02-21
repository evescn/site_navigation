from django.db import models


# Create your models here.
# python manage.py makemigrations
# python manage.py migrate

class Env(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, verbose_name="环境名称")

    class Meta:
        verbose_name_plural = "环境表"

    def __str__(self):
        return self.name


class Service(models.Model):
    sid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, verbose_name="服务名称")
    url = models.CharField(max_length=500, verbose_name="url地址")
    password_id = models.ForeignKey(to="Password", to_field='id', related_name='Password', on_delete=models.CASCADE,
                                    verbose_name="账户")
    env_id = models.ForeignKey(to="Env", to_field='id', on_delete=models.CASCADE, verbose_name="环境")

    class Meta:
        verbose_name_plural = "服务表"

    def __str__(self):
        return self.name


class Password(models.Model):
    user = models.CharField(max_length=100, verbose_name="用户名")
    password = models.CharField(max_length=100, null=True, blank=True, verbose_name="用户密码")

    # password_id = models.ForeignKey(to="Password", to_field='id', on_delete=models.CASCADE, verbose_name="密码")

    class Meta:
        verbose_name_plural = "用户表"

    def __str__(self):
        return self.user
