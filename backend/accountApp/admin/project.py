# _*_ coding: UTF-8 _*_
"""=====================================================
@IDE：PyCharm
@Author：Jacob
@Email：jacob1109@126.com
@Date：Jun 01, 2023 Thu 01:38 
@Desc：
====================================================="""
from django.contrib import admin

from Account.admin import BaseAdmin
from accountApp.forms import ProjectForm
from accountApp.models import ProjectModels


@admin.register(ProjectModels)
class ProjectAdmin(BaseAdmin):
    list_display = ("name", "_ForegroundAddress", "_LAA", "_username", "_pwd", "server", "db", '_operation')
    list_display_links = ("name", )
    search_fields = ("name", "username")
    list_filter = ("username", "group")
    form = ProjectForm

    def _ForegroundAddress(self, obj):
        if obj.ForegroundAddress is None:
            return "-"
        tag = BaseAdmin.username(obj.ForegroundAddress)
        return tag
    _ForegroundAddress.short_description = "前台地址"

    def _LAA(self, obj):
        if obj.LAA is None:
            return "-"
        tag = BaseAdmin.username(obj.LAA)
        return tag
    _LAA.short_description = "后台地址"

    def _username(self, obj):
        if obj.username is None:
            return '-'
        tag = BaseAdmin.username(obj.username)
        return tag
    _username.short_description = "后台管理账号"

    def _pwd(self, obj):
        if obj.pwd is None:
            return "-"
        tag = BaseAdmin.password(obj.pwd)
        return tag
    _pwd.short_description = "后台管理密码"

    def _operation(self, obj):
        tag = BaseAdmin.copyInfo(obj.get_copy_content)
        # FIXME: 这里如果添加showInfo会导致两个button显示两行，影响UI，所以暂时就加了Copy。需要解决此问题并添加showInfo
        """tag = BaseAdmin.copyInfo(obj.get_copy_content) + BaseAdmin.showInfo(obj.get_copy_content)"""
        return tag
    _operation.short_description = "操作"




