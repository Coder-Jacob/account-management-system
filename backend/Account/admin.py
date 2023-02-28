from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

LIST_DISPLAY = ['updatedAt', 'createdAt', 'deletedAt']


def showUrl(url):
    if url:
        tag = mark_safe('''<a href="%s" target="blank" class="button" title="%s">URL</a>''' % (url, url))
    else:
        tag = "-"
    return tag


def avatar(url):
    return format_html(
        '''<img src="{}" width="200px" height="100px"  title="点击可浏览" onClick="show_big_img(this)"/>''',
        url, )


class BaseAdmin(admin.ModelAdmin):
    list_display = LIST_DISPLAY
    date_hierarchy = 'updatedAt'

    @staticmethod
    def username(obj):
        tag = mark_safe(
            '''<div class="ui left labeled button" tabindex="0">
                    <a class="ui basic right pointing label" style="width:10em;">
                    %s
                    </a>
                    <div class="ui fade animated button blue" onclick="copyStr('%s')" tabindex="0" >
                        <div class="hidden content" style="color:white;" >Copy</div>
                        <div class="visible content">
                                <i class="copy icon"></i>
                        </div>
                    </div>
                </div>''' % (obj, obj))
        return tag

    @staticmethod
    def operation(obj):
        tag = mark_safe(
            '''
            <div class="ui buttons">
                <div class="ui disabled button" _msttexthash="7832253" _msthash="378"><i class="eye icon " style="opacity: 1"></i></div>
                <div class="or"></div>
                <div class="ui disabled blue button" _msttexthash="1952132" _msthash="379"><i class="copy icon " style="opacity: 1"></i></div>
            </div>
            ''')
        return tag

    @staticmethod
    def password(obj):
        tag = mark_safe(
            '''<div class="ui left labeled button" tabindex="0">
                    <a class="fade animated ui basic right pointing label">
                        ******
                    </a>
                    <div class="ui fade animated button blue" onclick="copyStr('%s')" >
                        <div class="hidden content" style="color:white;" >Copy</div>
                        <div class="visible content">
                                <i class="copy icon"></i>
                        </div>
                    </div>
                </div>''' % (obj,))
        return tag

    @staticmethod
    def shwoUrl(url: str):
        tag = mark_safe('''
                    <a class="ui circular icon red button" href="%s" target="blank">
                        <i class="linkify icon"></i>
                    </a>
            ''' % url)
        return tag

    class Media:

        def __init__(self):
            pass

        css = {
            'all': ('Semantic-UI-CSS-master/semantic.css',)
        }
        js = [
            'js/jquery-3.6.0.min.js',
            'Semantic-UI-CSS-master/semantic.js',
            'bootstrap-3.4.1-dist/js/bootstrap.js',
            'js/clipboardUtil.js',
        ]
        # 'js/clipboardUtil.js',


class PictureShowAdmin(BaseAdmin):
    def __init__(self, model, admin_site):
        self.list_display = super().list_display + ['_img']
        super().__init__(model, admin_site)

    def _img(self, obj):
        _url = ""
        if hasattr(obj, "originalUrl"):
            _url = obj.originalUrl
        if hasattr(obj, "cover"):
            if hasattr(obj.cover, "originalUrl"):
                _url = obj.cover.originalUrl
        return format_html(
            '''<img src="{}" width="200px" height="100px"  title="{}" onClick="show_big_img(this)"/>''',
            _url, "%s\n%s" %
                  (obj.__str__(), _url)

        )

    _img.short_description = "封面"

    class Media:
        js = (
            'js/jquery-3.6.0.min.js',
            'js/imageUtil.js'
        )
