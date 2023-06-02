# _*_ coding: UTF-8 _*_
"""=====================================================
@IDE：PyCharm
@Author：Jacob
@Email：jacob1109@126.com
@Date：Jun 01, 2023 Thu 01:18 
@Desc：
====================================================="""
from django.db import models

from . import DbService, Server
from .baseAccount import BaseAccount

class ProjectModels(BaseAccount):
    username = models.CharField(max_length=40, verbose_name="后台管理账号", null=True, blank=True)
    pwd = models.CharField(max_length=32, verbose_name="后台管理密码", null=True, blank=True)
    name = models.CharField(max_length=200, verbose_name="项目名")
    db = models.ForeignKey(to=DbService, verbose_name="绑定数据库", null=True, blank=True, on_delete=models.CASCADE)
    server = models.ForeignKey(to=Server, verbose_name="绑定服务器", null=True, blank=True, on_delete=models.CASCADE)
    LAA = models.CharField(max_length=200, verbose_name="后台地址", null=True, blank=True, help_text="如项目无后台可暂不填写！")
    ForegroundAddress = models.CharField(max_length=200, verbose_name="前台地址", null=True, blank=True, help_text="如项目无前台可暂不填写！")

    class Meta:
        verbose_name = "项目管理"
        verbose_name_plural = "所有" + verbose_name

    def get_copy_content(self):
        # content = f"WIFI管理信息({self.info})/jcb/WIFI名称：{self.name}/jcb/WIFI密码：{self.wifiPwd}/jcb/管理地址：{self.LAA}/jcb/管理员账号：{self.username}/jcb/管理员密码：{self.pwd}" if self.isAdmin else f"WIFI信息({self.info})/jcb/WIFI名称：{self.name}/jcb/WIFI密码：{self.wifiPwd}"
        return self.username
