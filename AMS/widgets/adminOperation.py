from django.contrib.admin.templatetags.admin_list import _boolean_icon
from django.forms import TextInput
from django.template.loader import render_to_string, get_template
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from ..models import ElasticSearch


class render_description():
    template_name = "widgets/operation.html"

    def render(self, name, value, attrs=None, renderer=None):
        context = self.get_context(name, value, attrs)
        template = get_template(self.template_name).render(context)
        return mark_safe(template)

# render_description.short_description = 'Description'  # 显示在列表标题中的名称
