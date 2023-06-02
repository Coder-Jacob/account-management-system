# _*_ coding: UTF-8 _*_
"""=====================================================
@IDE：PyCharm
@Author：Jacob
@Email：jacob1109@126.com
@Date：May 24, 2023 Wed 09:55 
@Desc：
====================================================="""
from django.db import models
from .baseAccount import BaseAccount

class Wifi(BaseAccount):
    username = models.CharField(max_length=40, verbose_name="管理员账号", null=True, blank=True, help_text="如您不是wifi管理员则不用填写！")
    pwd = models.CharField(max_length=32, verbose_name="密码", null=True, blank=True, help_text="如您不是wifi管理员则不用填写!")
    name = models.CharField(max_length=100, verbose_name="WIFI名", null=False, blank=False)
    wifiPwd = models.CharField(max_length=32, verbose_name="WIFI密码", null=True, blank=False)
    isAdmin = models.BooleanField(verbose_name="是否是管理员")
    LAA = models.CharField(max_length=100, verbose_name="管理地址", null=True, blank=True, help_text="如您不是wifi管理员则不用填写！")

    class Meta:
        verbose_name = "Wifi管理"
        verbose_name_plural = "所有" + verbose_name

    def __str__(self):
        return "WIFI：%s" % self.name

    def get_copy_content(self):
        content = f"WIFI管理信息({self.info})/jcb/WIFI名称：{self.name}/jcb/WIFI密码：{self.wifiPwd}/jcb/管理地址：{self.LAA}/jcb/管理员账号：{self.username}/jcb/管理员密码：{self.pwd}" if self.isAdmin else f"WIFI信息({self.info})/jcb/WIFI名称：{self.name}/jcb/WIFI密码：{self.wifiPwd}"
        return content
