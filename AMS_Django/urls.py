"""AMS_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import re_path as url
# from django.views.generic.base import RedirectView
# from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.static import serve as STATIC_SERVER

import AMS.views
from . import settings
from django.urls import path

admin.site.site_header = 'VaultKey'
admin.site.site_title = 'VaultKey账号管理系统'

urlpatterns = [
    path('admin/AMS/accountlist', AMS.views.AccountList),
    path('', admin.site.urls),
    path('account/', include('AMS.urls')),
    url('^static/(?P<path>.*)$', STATIC_SERVER, {'document_root': settings.STATIC_ROOT, 'show_indexes': True}, name='static'),
    # path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico')))


]
