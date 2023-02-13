from django.contrib import admin
from accountApp.models import BankCardModels
from Account.admin import LIST_DISPLAY, BaseAdmin


@admin.register(BankCardModels)
class BankCardAdmin(BaseAdmin):
    list_display = ['_cardNum', '_withdrawalPwd', '_EbankingPwd', '_tel', 'affiliatedBank', 'bankCardType', 'group',
                    'remark', 'deletedAt',  'createdAt', 'updatedAt']
    list_display_links = ['_cardNum', 'affiliatedBank', '_tel']
    date_hierarchy = 'updatedAt'
    search_fields = ['_cardNum', '_tel', 'remark', ]
    list_filter = ['tel', 'group', 'affiliatedBank', 'bankCardType']
    list_select_related = ['tel', 'group']
    autocomplete_fields = ['tel', 'group']
    list_per_page = 8
    actions = []

    def _cardNum(self, obj):
        return BaseAdmin.username(obj.id)

    def _withdrawalPwd(self, obj):
        return BaseAdmin.password(obj.withdrawalPwd)

    def _EbankingPwd(self, obj):
        return BaseAdmin.password(obj.E_bankingPwd)

    def _tel(self, obj):
        return BaseAdmin.username(obj.tel.content)
