from django.contrib import admin

from Account.admin import BaseAdmin
from ..forms import ServerForm
from ..models import Server


@admin.register(Server)
class ServerAdmin(BaseAdmin):
    list_display = ['remark', "_ip", '_password', 'ssh', '_biosPassword', 'group', 'hoster', '_operation']
    list_display_links = ['remark', 'group', 'hoster']
    list_filter = ['group', 'hoster', 'ssh']
    date_hierarchy = 'updatedAt'
    search_fields = ['ip', 'remark', 'hoster']
    search_help_text = ['你好，这是搜索帮助语句！']
    autocomplete_fields = ['group']
    form = ServerForm

    # FIXME: 这里出现的BUG在forms/serverUser.py已指出，问题解决好了可以用此功能
    # inlines = [ServerUserInlineAdmin]

    def _operation(self, obj):
        tag = BaseAdmin.copyInfo(obj.get_copy_content()) + BaseAdmin.showInfo(obj.get_copy_content())
        return tag
    _operation.short_description = 'operation'

    def _ip(self, obj):
        return BaseAdmin.username(obj.ip)

    def _password(self, obj):
        return BaseAdmin.password(obj.rootPassword)

    _password.short_description = "root密码"

    def _biosPassword(self, obj):
        return BaseAdmin.password(obj.bios)

    _biosPassword.short_description = "BIOS密码"

    class Media:

        def __init__(self):
            pass

        css = {
        }
        js = [
        ]
