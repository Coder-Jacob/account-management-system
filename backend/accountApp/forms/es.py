# _*_ codign:utf8 _*_
"""====================================
@Author:Jacob
@Email：jacob1109@126.com
@Date：2023/2/14
@Software: PyCharm
@disc:
======================================="""
from django.forms import ModelForm

from accountApp.fields import SdmPasswordField
from accountApp.models import ElasticSearch


class ElasticSearchForm(ModelForm):
    # FIXME：这里的password在InlineAdmin中也需要输入，而且是必填，但是因为实际实用不便为由暂时搁置了，需要及时处理。
    # rootPassword = SdmPasswordField(label="ROOT密码", required=False, encryptByMd5=False)
    # bios = SdmPasswordField(label="BIOS密码", required=False, encryptByMd5=False)

    class Meta:
        model = ElasticSearch
        fields = ['server', 'port', 'elasticPwd', 'kibanaPwd', 'apmPwd', 'beatsPwd', 'logstashPwd', 'remoteMonitoringPwd', 'remark', 'info']


# class ServerUserForm(ServerFormBase):
#     password = SdmPasswordField(label="密码", required=True, encryptByMd5=False)
