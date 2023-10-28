# _*_ coding: UTF-8 _*_
"""=====================================================
@IDE：PyCharm
@Author：Jacob
@Email：jacob1109@126.com
@Date：May 24, 2023 Wed 10:16 
@Desc：
====================================================="""
from django.contrib import admin

from AMS_Django.admin import BaseAdmin
from AMS.forms import WifiForm
from AMS.models import Wifi


@admin.register(Wifi)
class WifiAdmin(BaseAdmin):
    list_display = ("name", "_wifiPwd", "isAdmin", "_LAA", "_username", "_pwd", "_operation")
    list_display_links = ("name",)
    search_fields = ("name", "username",)
    list_filter = ("isAdmin", "LAA")
    form = WifiForm

    def _wifiPwd(self, obj):
        return BaseAdmin.username(obj.wifiPwd)

    _wifiPwd.short_description = "WIFI密码"

    def _LAA(self, obj):
        if obj.LAA is None:
            return "-"
        return BaseAdmin.showUrl((obj.name + "wifi管理地址"), obj.LAA)

    _LAA.short_description = "管理地址"

    def _username(self, obj):
        if obj.username is None:
            return "-"
        return BaseAdmin.username(obj.username)

    _username.short_description = "管理员账号"

    def _pwd(self, obj):
        if obj.pwd is None:
            return "-"
        return BaseAdmin.password(obj.pwd)

    _pwd.short_description = "管理员密码"

    def _operation(self, obj):
        # FIXME: 这里copyInfo和showInfo先给了wifi名，后续需要在models.py文件添加get_copy_content()方法来获取完整的复制和查看信息（getInformation()）
        tag = BaseAdmin.copyInfo(obj.get_copy_content()) + BaseAdmin.showInfo(obj.name)
        return tag

    _operation.short_description = "操作"
