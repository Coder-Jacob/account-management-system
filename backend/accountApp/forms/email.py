from django.forms import ModelForm

from accountApp.fields import SdmPasswordField
from accountApp.models import Email


class EmailForm(ModelForm):
    pwd = SdmPasswordField(label="密码", required=True, encryptByMd5=False)

    class Meta:
        model = Email

        fields = ['username', 'pwd', "psi", 'group', 'remark', 'info']
