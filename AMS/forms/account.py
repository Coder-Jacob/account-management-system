from django.forms import ModelForm

from AMS.fields import SdmPasswordField
from AMS.models import Account


class AccountForm(ModelForm):
    # FIXME：这里的password在InlineAdmin中也需要输入，而且是必填，但是因为实际实用不便为由暂时搁置了，需要及时处理。
    pwd = SdmPasswordField(label="密码", required=False, encryptByMd5=False)
    class Meta:
        model = Account
        fields = ['name', 'url', 'username', 'pwd',  'tels', 'emails', 'wechat', 'group', 'info']
