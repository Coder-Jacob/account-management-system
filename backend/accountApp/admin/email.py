from django.contrib import admin
from accountApp.forms import EmailForm
from accountApp.models import Email
from Account.admin import LIST_DISPLAY, BaseAdmin


# Register your admin models here.


@admin.register(Email)
class EmailAdmin(BaseAdmin):
    list_display = ['id', '_username', '_pwd', "_PSI", 'group', 'remark'] + LIST_DISPLAY
    list_display_links = ['id']
    list_filter = ['group']
    list_select_related = ['group']
    search_fields = ['_username', 'remark', 'group__name']
    form = EmailForm

    def _username(self, obj):
        return BaseAdmin.username(obj.username, width='12em')

    def _pwd(self, obj):
        return BaseAdmin.password(obj.pwd)

    def _PSI(self, obj):
        if obj.psi is None:
            return obj.psi
        return BaseAdmin.password(obj.psi)
    _PSI.short_description = 'POP3/SMTP/IMAP授权码'
