from django.db import models

from .human import Human
from .base import BaseServiceModel


class DbService(BaseServiceModel):
    pwd = models.CharField(verbose_name="root密码", max_length=48, null=True, blank=True)
    typeOpts = (
        (0, 'MySQL'),
        (1, 'PostgreSQL')
    )
    ttype = models.IntegerField(verbose_name='数据库类型', choices=typeOpts, default=0, null=False, blank=False, db_index=True)
    group = models.ForeignKey(verbose_name="所属个体/组织", to=Human, on_delete=models.CASCADE, null=True, blank=False)

    class Meta:
            verbose_name = "数据服务"
            verbose_name_plural = f"所有{verbose_name}"

    def __str__(self):
        return f"{self.typeOpts[self.ttype][1]}数据{super().__str__()}"

    def get_copy_content(self):
        username = 'root'
        dbType = 'MySQL'
        if self.ttype == 1:
            username = 'postgres'
            dbType = 'PostgreSQL'
        content = f"{dbType}数据库（{self.group.name}）/jcb/地址：{self.server.ip}:{self.port}/jcb/root用户名：{username}/jcb/root密码：{self.pwd}/jcb/宿主服务器：{self.server.remark}（{self.server.ip}）/jcb/备注：{self.remark}"
        return content
