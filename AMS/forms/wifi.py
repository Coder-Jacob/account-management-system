from django.forms import ModelForm

from AMS.fields import SdmPasswordField
from AMS.models import Wifi


class WifiForm(ModelForm):
    pwd = SdmPasswordField(label="管理员密码", required=False, encryptByMd5=False)
    wifiPwd = SdmPasswordField(label="Wifi密码", required=True, encryptByMd5=False)

    class Meta:
        model = Wifi
        fields = ['name', "wifiPwd", 'group', 'isAdmin', 'LAA', 'username', 'pwd', 'info']
