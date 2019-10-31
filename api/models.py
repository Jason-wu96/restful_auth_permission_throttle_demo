from django.db import models


class UserInfo(models.Model):
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
    user_type_choices = (
        (1, '普通用户'),
        (2, 'vip'),
        (3, 'suvip')
    )
    user_type = models.IntegerField(choices=user_type_choices)


class Token(models.Model):
    token = models.CharField(max_length=64)
    user = models.OneToOneField(to=UserInfo, on_delete=models.CASCADE)
