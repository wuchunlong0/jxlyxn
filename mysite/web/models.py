# -*- coding: UTF-8 -*-
from django.db import models


class Customer(models.Model):
    """
    客户表
    """
    name = models.CharField(verbose_name='姓名', max_length=32)
    year = models.CharField(verbose_name='出生年月', max_length=32)
    sex = models.CharField(verbose_name='性别', max_length=32)
    tel = models.CharField(verbose_name='联系电话', max_length=32)

    def __str__(self):
        return self.name

class Payment(models.Model):
    """
    付费记录
    """
    customer = models.ForeignKey(verbose_name='关联客户', to='Customer')
    money = models.IntegerField(verbose_name='付费金额')
    create_time = models.DateTimeField(verbose_name='付费时间', auto_now_add=True)


