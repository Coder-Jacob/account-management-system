from django.forms import ModelForm

from accountApp.fields import SdmPasswordField
from accountApp.models import Human


class HumanForm(ModelForm):
    class Meta:
        model = Human

        fields = ['name', 'info']
