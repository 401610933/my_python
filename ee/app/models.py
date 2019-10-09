from django.db import models


class test(models.Model):
    username = models.CharField(max_length=20)
    age = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    regtime = models.CharField(max_length=20)


class user(models.Model):
    username = models.CharField(max_length=20)
    regtime = models.CharField(max_length=20)
    money = models.CharField(max_length=20)