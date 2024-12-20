# _*_ coding: UTF-8 _*_
"""=====================================================
@IDE：PyCharm
@Author：Jacob
@Email：jacob1109@126.com
@Date：2023/12/08
@Description：
====================================================="""
from django.db import models

from AMS_Django.models import BaseModel

class ClassifyModel(BaseModel):
    name = models.CharField(max_length=50, verbose_name="分类名称", default="未知分类")

    class Meta:
        verbose_name = "账号分类"
        verbose_name_plural = "所有" + verbose_name
        db_table = "account_classify"

    def __str__(self):
        return self.name
