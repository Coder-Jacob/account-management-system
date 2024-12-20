from django.forms import ModelForm

from AMS.fields import SdmPasswordField
from AMS.models import Email


class EmailForm(ModelForm):
    pwd = SdmPasswordField(label="密码", required=True, encryptByMd5=False)

    class Meta:
        model = Email

        fields = ['username', 'pwd', 'group', 'remark', 'info']
