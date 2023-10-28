from django.contrib import admin
from django.utils.safestring import mark_safe

from AMS.forms import AccountForm
from AMS.models import Account, Tel, Email
from AMS_Django.admin import BaseAdmin


@admin.register(Account)
class AccountAdmin(BaseAdmin):
    list_display = ['_name', '_username', '_password', '_tels', '_emails', '_wechat', '_operation']
    list_display_links = ['_name']
    date_hierarchy = 'updatedAt'
    search_fields = ['name', 'username', 'url', 'info']
    list_filter = ['group', 'tels', 'emails', 'wechat']
    list_select_related = ['group', 'wechat']
    autocomplete_fields = ['tels', 'emails', 'wechat', 'group']
    list_per_page = 8
    actions = []
    form = AccountForm

    def _operation(self, obj):
        tag = BaseAdmin.showUrl(obj.name, obj.url) + BaseAdmin.copyInfo(obj.get_copy_content()) + BaseAdmin.showInfo(
            obj.get_copy_content())
        return tag

    _operation.short_description = 'operation'

    def _password(self, obj):
        return BaseAdmin.password(obj.pwd)

    _password.allow_tags = True

    def _username(self, obj):
        return BaseAdmin.username(obj.username)

    _username.allow_tags = True

    def _name(self, obj):
        # tag = mark_safe('''<a class="ui teal label" style="white-space:nowrap;" onclick="goToDetail(this)"><i class="mail icon"></i>%s</a>''' % obj.name)
        return obj.name
    _name.short_description = 'WebsiteName'

    def _wechat(self, obj):
        return obj.wechat
    _wechat.short_description = "wechat"

    def _tels(self, obj):
        items = self._getTelItem('-') if obj.tels is None else self._getTelItem(obj.tels)
        finalList = '''
                <div class="ui list">
                    %s              
                </div>
        ''' % items
        return mark_safe(finalList)

    def _getTelItem(self, tel):
        item = '''
                <div class="item">
                    <i class="phone square icon"></i>
                    <div class="content">
                        <a class="header">%s</a>
                    </div>
                </div>
                ''' % tel
        return mark_safe(item)

    def _emails(self, obj: Account):
        items = self._getEmailItem('-') if obj.emails is None else self._getEmailItem(obj.emails)
        finalList = '''
                <div class="ui list">
                    %s              
                </div>
        ''' % items
        return mark_safe(finalList)

    def _getEmailItem(self, email):
        item = '''
                <div class="item">
                    <i class="mail icon"></i>
                    <div class="content">
                        <a class="header">%s</a>
                    </div>
                </div>
                ''' % email
        return mark_safe(item)

    class Media:

        def __init__(self):
            pass

        css = {
        }
        js = [
        ]
