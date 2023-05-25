from django.contrib import admin

from accountApp.forms import WechatForm
from accountApp.models import Wechat, Email
from Account.admin import LIST_DISPLAY, BaseAdmin


@admin.register(Wechat)
class WechatAdmin(BaseAdmin):
    list_display = ['_remark', 'nickName', '_id', '_tel', '_password', '_email', 'group', 'remark']
    list_display_links = ['_remark', '_id', 'nickName']
    date_hierarchy = 'updatedAt'
    search_fields = ['id', 'nickName', 'remark', '_email', ]
    list_filter = ['tel', 'group']
    list_select_related = list_filter
    autocomplete_fields = ['tel', 'group']
    list_per_page = 8
    actions = []
    form = WechatForm

    def _remark(self, obj):
        return Wechat.getRemark(obj)
    _remark.short_description = '说明'

    def _id(self, obj):
        return BaseAdmin.username(obj.id)

    def _password(self, obj):
        return BaseAdmin.password(obj.pwd)

    def _tel(self, obj):
        return BaseAdmin.username(obj.tel.content)

    def _email(self, obj):
        return Email.getEmails(obj.email)
