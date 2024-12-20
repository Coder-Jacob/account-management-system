from django.forms import ModelForm

from AMS.fields import SdmPasswordField
from AMS.models import BankCard


class BankCardForm(ModelForm):
    E_bankingPwd = SdmPasswordField(label="网银密码", required=False, encryptByMd5=False)

    class Meta:
        model = BankCard
        fields = ['cardNumber', 'withdrawalPwd', 'E_bankingPwd', 'tel',  'affiliatedBank', 'bankCardType', 'group', 'remark', 'info']
