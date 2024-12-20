from django.db import models

from AMS_Django.models import BaseModel
from .human import Human


class Server(BaseModel):
    group = models.ForeignKey(verbose_name="所属个体/组织", to=Human, on_delete=models.CASCADE, null=True, blank=True)
    ip = models.GenericIPAddressField(verbose_name="IP地址", null=False, blank=False, unique=False, help_text="可以是IPV4/IPV6")
    rootUsername = models.CharField(max_length=32, verbose_name="root用户名", blank=False, default="root")
    rootPassword = models.CharField(max_length=32, verbose_name="root密码", blank=False, null=True)
    hosterOptions = (
        (1, '本地环境'),
        (2, '阿里云'),
        (3, '腾讯云'),
        (4, '微信云开发'),
        (5, '微信云托管')
    )
    hoster = models.PositiveSmallIntegerField(choices=hosterOptions, null=True, blank=False, verbose_name="托管方")
    bios = models.CharField(verbose_name="BIOS", max_length=32, null=True, blank=True)
    ssh = models.IntegerField(verbose_name="SSH端口", default=22, blank=True)
    mac = models.CharField(max_length=17, verbose_name="MAC地址", blank=True, null=True)
    remark = models.CharField(verbose_name="NAME", max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "服务器"
        verbose_name_plural = f"所有{verbose_name}"

    def __str__(self):
        return f"服务器（{self.ip},{self.remark}）"

    def get_copy_content(self):
        hosters = dict(self.hosterOptions)[self.hoster]
        content = f"{self.remark}（服务器信息）/jcb/地址：{self.ip}:{self.ssh}/jcb/root用户名：{self.rootUsername}/jcb/root密码：{self.rootPassword}/jcb/BIOS密码：{self.bios}/jcb/MAC地址：{self.mac}/jcb/所属个体/企业：{self.group.name}/jcb/托管方：{hosters}"
        return content
