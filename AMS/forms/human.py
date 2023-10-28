from django.forms import ModelForm

from AMS.fields import SdmPasswordField
from AMS.models import Human


class HumanForm(ModelForm):
    class Meta:
        model = Human

        fields = ['name', 'info']
