from django.contrib.auth.models import User
from django.db import models


# from django.utils import timezone

# Create your models here.

# 账号菜单
class parentMenu(models.Model):
    name = models.CharField(max_length=200, verbose_name='菜单名')
    icon = models.CharField(max_length=100, verbose_name='图标', null=True, blank=True)

    class Meta:
        verbose_name = '账号菜单'
        verbose_name_plural = '%s' % verbose_name

    def __str__(self):
        return self.name


class enterprices(models.Model):
    name = models.CharField(max_length=200, verbose_name='企业/分类名')

    class Meta:
        verbose_name = '企业/分类'
        verbose_name_plural = '%s' % verbose_name

    def __str__(self):
        return self.name


# 账号管理
class Account(models.Model):
    userName = models.CharField(max_length=200, verbose_name='账号')
    Pwd = models.CharField(max_length=200, verbose_name='密码')
    ipAddres = models.GenericIPAddressField(verbose_name='IP', null=True, blank=True)
    port = models.IntegerField(verbose_name='端口号', null=True, blank=True)
    Platform = models.CharField(max_length=100, verbose_name='平台', blank=True, null=True)
    enterprice = models.ForeignKey(to=enterprices, on_delete=models.CASCADE, verbose_name='企业/分类')
    remarks = models.CharField(max_length=200, verbose_name='备注', null=True, blank=True)
    Links = models.CharField(max_length=100, verbose_name='链接', null=True, blank=True)
    BasicAuthUser = models.CharField(max_length=255, verbose_name='BasicAuth用户名', null=True, blank=True)
    BasicAuthPwd = models.CharField(max_length=255, verbose_name='BasicAuth密码', null=True, blank=True)
    ParentMenu = models.ForeignKey(to=parentMenu, on_delete=models.CASCADE, verbose_name="账号类型")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='操作用户')  # 作者
    create_time = models.DateTimeField(auto_now_add=True)  # 创建时间
    update_time = models.DateTimeField(auto_now=True)  # 更新时间

    class Meta:
        verbose_name = '所有账号'
        verbose_name_plural = '%s' % verbose_name
        ordering = ['id']  # 配置排序

    def __str__(self):
        return self.userName
