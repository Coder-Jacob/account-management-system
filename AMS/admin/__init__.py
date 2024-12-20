from django.contrib import admin

from AMS_Django.admin import LIST_DISPLAY
from .account import AccountAdmin, Account
from .bt import BtAdmin
from .dbService import DbServiceAdmin
from .dbServiceUser import DbServiceUserAdmin
from .email import EmailAdmin
from .es import ElasticSearchAdmin
from .server import ServerAdmin
from .wifi import WifiAdmin
from .serverUser import ServerUserAdmin
from .tel import TelAdmin
from .bankCard import BankCardAdmin
from .wechat import WechatAdmin
from .project import ProjectAdmin
from ..forms import HumanForm
# Register your admin models here.
from ..models import Human, ClassifyModel

@admin.register(Human)
class GroupAdmin(admin.ModelAdmin):
    list_display =["__str__"] + LIST_DISPLAY
    search_fields = ['name']
    list_per_page = 14
    form = HumanForm
    # def _count(self, obj):
    #     return AMS_Django.objects.filter(types=obj.id).count()
@admin.register(ClassifyModel)
class ClassifyAdmin(admin.ModelAdmin):
    list_display = ["__str__"] + LIST_DISPLAY
    search_fields = ['name']
    list_per_page = 14
