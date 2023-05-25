from django.db import models

from Account.models import BaseModel
from .human import Human


class Tel(BaseModel):
    content = models.CharField(max_length=11, unique=True, null=False, blank=True, verbose_name='手机号')
    ldPwd = models.CharField(max_length=10, null=True, blank=True, default='无', verbose_name='业务密码')
    appPwd = models.CharField(max_length=100, null=True, blank=True, verbose_name='app登录密码')
    remark = models.CharField(max_length=100, null=True, blank=True, verbose_name='备注')
    owner = models.ForeignKey(verbose_name="所属个体/组织", to=Human, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "手机号"
        verbose_name_plural = "所有" + verbose_name

    def __str__(self):
        if self.remark is None:
            return "%s" % self.content
        else:
            return "%s(%s)" % (self.content, self.remark)

    def get_content(self):
        return self.content
