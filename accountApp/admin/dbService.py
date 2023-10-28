from django.contrib import admin

from Account.admin import LIST_DISPLAY, BaseAdmin
from ..forms import DbServiceForm
from ..models import DbService


@admin.register(DbService)
class DbServiceAdmin(BaseAdmin):
    form = DbServiceForm
    list_display = ['server', '_link', '_username', '_password', 'port', 'ttype', 'group', 'remark', '_operation']
    list_display_links = ['server', 'port', 'ttype']
    list_filter = ['server', 'port', 'ttype']
    date_hierarchy = 'updatedAt'
    search_fields = ['rootPwd.password', 'remark']
    search_help_text = ['你好，这是搜索帮助语句！']
    autocomplete_fields = ['server']

    # FIXME: 这里出现的BUG在forms/serverUser.py已指出，问题解决好了可以用此功能
    # inlines = [DbServiceUserInlineAdmin]

    def _password(self, obj):
        return BaseAdmin.password(obj.pwd)

    _password.short_description = "root密码"

    def _link(self, obj):
        return BaseAdmin.username(f'{obj.server.ip}:{obj.port}')

    def _username(self, obj):
        username = 'root'
        if obj.ttype == 1:
            username = 'postgres'
        return BaseAdmin.username(username, width='6em')
    _username.short_description = "用户名"

    def _operation(self, obj):
        tag = BaseAdmin.copyInfo(obj.get_copy_content()) + BaseAdmin.showInfo(obj.get_copy_content())
        return tag
    _operation.short_description = 'operation'
