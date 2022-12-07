from django.contrib import admin
from . import models
# from Account.menusql import data

# Register your models here.

# 浏览器标签栏Title
admin.site.site_title = 'Spider账号管理系统'
# 登录页导航条和首页导航条标题
admin.site.site_header = 'Spider账号管理系统'
# 主页标题
admin.site.index_title = '欢迎登录'


@admin.register(models.parentMenu)
class ClassifyAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')


@admin.register(models.enterprices)
class entprcAdmin(admin.ModelAdmin):
    list_display = ('name',)


# 丝路融创
@admin.register(models.Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('userName', 'Pwd', 'Links', 'Platform', 'remarks')
    list_filter = ('userName', 'Platform', 'remarks')

    class Media:
        css = {
            'all': ('Account/admin/style.css',)
        }
