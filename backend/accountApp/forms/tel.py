from django.forms import ModelForm

from accountApp.fields import SdmPasswordField
from accountApp.models import Tel


class TelForm(ModelForm):
    appPwd = SdmPasswordField(label="APP密码", required=False, encryptByMd5=False)

    class Meta:
        model = Tel

        fields = ['content', 'ldPwd', 'appPwd', 'owner', 'remark']
