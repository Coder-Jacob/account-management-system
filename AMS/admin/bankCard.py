from django.contrib import admin

from AMS.forms import BankCardForm
from AMS.models import BankCard
from AMS_Django.admin import LIST_DISPLAY, BaseAdmin


@admin.register(BankCard)
class BankCardAdmin(BaseAdmin):
    list_display = ['affiliatedBank', '_cardNum', '_tel', '_withdrawalPwd', '_EbankingPwd', 'bankCardType', 'group', '_operation']
    list_display_links = ['affiliatedBank']
    search_fields = ['_cardNum', '_tel', 'remark', ]
    list_filter = ['tel', 'group', 'affiliatedBank', 'bankCardType']
    list_select_related = ['tel', 'group']
    autocomplete_fields = ['tel', 'group']
    list_per_page = 8
    actions = []
    form = BankCardForm

    def _operation(self, obj):
        tag = BaseAdmin.copyInfo(obj.get_copy_content()) + BaseAdmin.showInfo(obj.get_copy_content())
        return tag
    _operation.short_description = 'operation'

    def _cardNum(self, obj):
        return BaseAdmin.username(obj.cardNumber, width='13em')

    _cardNum.short_description = "cardNum"

    def _withdrawalPwd(self, obj):
        return BaseAdmin.password(obj.withdrawalPwd)

    _withdrawalPwd.short_description = 'pwd'

    def _EbankingPwd(self, obj):
        return BaseAdmin.password(obj.E_bankingPwd)

    _EbankingPwd.short_description = 'e_pwd'

    def _tel(self, obj):
        return BaseAdmin.username(obj.tel.content, width='8em')

    _tel.short_description = 'tel'
