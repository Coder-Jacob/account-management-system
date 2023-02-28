from django.contrib import admin

from accountApp.models.type import Type
from Account.admin import LIST_DISPLAY
from .account import AccountAdmin, Account
from .bt import BtAdmin
from .dbService import DbServiceAdmin
from .dbServiceUser import DbServiceUserAdmin
from .email import EmailAdmin
from .es import ElasticSearchAdmin
from .server import ServerAdmin
from .serverUser import ServerUserAdmin
from .tel import TelAdmin
from .bankCard import BankCardAdmin
from .wechat import WechatAdmin
# Register your admin models here.
from ..models import Human


@admin.register(Human, Type)
class GroupAdmin(admin.ModelAdmin):
    list_display =["__str__", '_count'] + LIST_DISPLAY
    search_fields = ['name']
    list_per_page = 14

    def _count(self, obj):
        return Account.objects.filter(types=obj.id).count()
