from django.db import models

from .classify import ClassifyModel
from .baseAccount import BaseAccount
from .email import Email
from .tel import Tel
from .wechat import Wechat


class Account(BaseAccount):
    tels = models.ForeignKey(verbose_name="所有绑定的手机号", to=Tel, on_delete=models.CASCADE, related_name="tels", blank=True, null=True)
    emails = models.ForeignKey(verbose_name="所有绑定的电子邮箱", to=Email, on_delete=models.CASCADE, related_name="emails", blank=True, null=True)
    wechat = models.ForeignKey(verbose_name='绑定的微信', blank=True, null=True, on_delete=models.CASCADE, to=Wechat)
    name = models.CharField(max_length=50, verbose_name="网站名称", null=True, blank=True)
    url = models.URLField(verbose_name="网站地址", null=True, blank=True)
    classify = models.ForeignKey(verbose_name="分类", to=ClassifyModel, on_delete=models.CASCADE, null=True, blank=False)

    class Meta:
            verbose_name = "通用账号"
            verbose_name_plural = "所有" + verbose_name

    def __str__(self):
        return "%s账号" % self.name

    def get_copy_content(self):
        content = f"{self.name}（{self.group.name}）/jcb/用户名：{self.username}/jcb/密码：{self.pwd}/jcb/绑定手机号：{'-' if self.tels is None else self.tels}/jcb/绑定邮箱：{'-' if self.emails is None else self.emails}/jcb/绑定微信：{'-' if self.wechat is None else self.wechat.id}/jcb/访问链接：{self.url}"
        return content



