from django.db import models

from .base import BaseServiceUserModel
from .dbService import DbService
from .human import Human


class DbServiceUser(BaseServiceUserModel):
    server = models.ForeignKey(to=DbService, on_delete=models.CASCADE, verbose_name="服务器", null=True, blank=False)


    class Meta:
        verbose_name = "数据库用户"
        verbose_name_plural = f"所有{verbose_name}"

    def __str__(self):
        return f"{self.server.typeOpts[self.server.ttype][1]}数据用户（{self.server.server.ip}-{self.owner}）"

    def get_copy_content(self):
        content = f"{self.__str__()}/jcb/地址：{self.server.server.ip}:{self.server.port}/jcb/root用户名：{self.username}/jcb/密码：{self.password}"
        return content
