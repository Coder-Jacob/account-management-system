from django.contrib import admin

from Account.admin import LIST_DISPLAY, BaseAdmin
from ..forms import DbServiceUserForm, DbServiceUserFormBase
from ..models import DbServiceUser


@admin.register(DbServiceUser)
class DbServiceUserAdmin(BaseAdmin):
    list_display = ['server', '_username', '_password', 'hasRootPriority', 'owner', '_operation']
    autocomplete_fields = ['server', 'owner']
    list_filter = ['hasRootPriority', 'server', 'owner']
    list_select_related = autocomplete_fields
    raw_id_fields = ('owner', 'server')
    form = DbServiceUserForm

    def _username(self, obj):
        return BaseAdmin.username(obj.username)

    def _password(self, obj):
        return BaseAdmin.password(obj.password)
    _password.short_description = "密码"

    def _operation(self, obj):
        tag = BaseAdmin.copyInfo(obj.get_copy_content()) + BaseAdmin.showInfo(obj.get_copy_content())
        return tag
    _operation.short_description = 'operation'


# FIXME: 出现form页面下方的list每一行上面出现model __str__(): 函数返回的值，导致页面不美观的问题，所以暂时去掉此功能。后期得解决
# class DbServiceUserInlineAdmin(admin.TabularInline):
#     model = DbServiceUser
#     autocomplete_fields = ['server', 'owner']
#     exclude = ('password',)
#     min_num = 0
#     extra = 0
#     form = DbServiceUserFormBase
