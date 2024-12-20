from django.contrib import admin
from AMS_Django.admin import LIST_DISPLAY, BaseAdmin
from ..forms import TelForm
from ..models import Tel


@admin.register(Tel)
class TelAdmin(BaseAdmin):
    list_display = ['content', '_ldPwd', '_appPwd', 'owner', 'remark']
    list_display_links = ['content']
    list_filter = ['owner']
    autocomplete_fields = ['owner']
    list_select_related = ['owner']
    search_fields = ['content']
    form = TelForm

    def _ldPwd(self, obj):
        if obj.ldPwd == '无' or obj.ldPwd is None:
            return obj.ldPwd
        return BaseAdmin.username(obj.ldPwd)

    _ldPwd.short_description = '业务密码'

    def _appPwd(self, obj):
        print(obj.appPwd)
        if obj.appPwd is None or obj.appPwd == '':
            return '-'
        return BaseAdmin.password(obj.appPwd)

    _appPwd.short_description = 'APP密码'
