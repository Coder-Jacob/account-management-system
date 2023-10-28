from django.forms import ModelForm

from accountApp.fields import SdmPasswordField
from accountApp.models import Wechat


class WechatForm(ModelForm):
    pwd = SdmPasswordField(label="密码", required=True, encryptByMd5=False)

    class Meta:
        model = Wechat
        fields = ['id', 'nickName', "pwd", 'tel', 'email', 'group', 'remark', 'info']
