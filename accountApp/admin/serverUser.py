from django.contrib import admin
from Account.admin import LIST_DISPLAY, BaseAdmin
from ..forms import ServerUserForm
from ..models import ServerUser


@admin.register(ServerUser)
class ServerUserAdmin(BaseAdmin):
    list_display = ['server', '_username', '_password', 'owner', 'hasRootPriority', 'updatedAt', 'createdAt', '_operation']
    autocomplete_fields = ['server', 'owner']
    list_filter = ['hasRootPriority', 'server', 'owner']
    list_select_related = autocomplete_fields
    form = ServerUserForm

    def _operation(self, obj):
        tag = BaseAdmin.copyInfo(obj.get_copy_content()) + BaseAdmin.showInfo(obj.get_copy_content())
        return tag
    _operation.short_description = 'operation'

    def _username(self, obj):
        return BaseAdmin.username(obj.username)

    def _password(self, obj):
        return BaseAdmin.password(obj.pwd)


# FIXME: 出现form页面下方的list每一行上面出现model __str__(): 函数返回的值，导致页面不美观的问题，所以暂时去掉此功能。后期得解决
# class ServerUserInlineAdmin(admin.TabularInline):
#     model = ServerUser
#     form = ServerUserForm
#     autocomplete_fields = ['server', 'owner']
#     min_num = 0
#     extra = 1
#     verbose_name_plural = ''
#     verbose_name = ''



