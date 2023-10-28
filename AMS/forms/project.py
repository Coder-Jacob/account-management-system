# _*_ coding: UTF-8 _*_
"""=====================================================
@IDE：PyCharm
@Author：Jacob
@Email：jacob1109@126.com
@Date：Jun 01, 2023 Thu 02:03 
@Desc：
====================================================="""
from django.forms import ModelForm

from AMS.fields import SdmPasswordField
from AMS.models import ProjectModels

class ProjectForm(ModelForm):
    pwd = SdmPasswordField(label="后台管理密码", encryptByMd5=False, required=False)

    class Meta:
        model = ProjectModels
        fields = ["name", "group", "ForegroundAddress", "LAA", "username", "pwd", "server", "db", "info"]
