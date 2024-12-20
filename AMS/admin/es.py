from django.contrib import admin

from .base import BaseServiceAdmin
from ..models import ElasticSearch
from ..forms import ElasticSearchForm
from ..widgets import render_description
@admin.register(ElasticSearch)
class ElasticSearchAdmin(BaseServiceAdmin):
    list_display = ['remark', 'ip', 'port', '_elastic', '_kibana_system', '_apm_system', '_beats_system', 'createdAt', 'updatedAt', '_operation']
    list_display_links = ['remark']
    form = ElasticSearchForm

    def _elastic(self, obj):
        return BaseServiceAdmin.password(obj.elasticPwd)

    def _kibana_system(self, obj):
        return BaseServiceAdmin.password(obj.kibanaPwd)

    def _apm_system(self, obj):
        return BaseServiceAdmin.password(obj.apmPwd)

    def _beats_system(self, obj):
        return BaseServiceAdmin.password(obj.beatsPwd)

    def ip(self, obj):
        return BaseServiceAdmin.username(obj.server.ip)

    def _operation(self, obj):
        return BaseServiceAdmin.operation(obj.server.ip)
        # return OperationInput

    _operation.short_description = "操作"
