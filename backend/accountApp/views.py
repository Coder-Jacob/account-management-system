from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Account
import time
from datetime import datetime
from django.views import View


# Create your views here.
def AccountList(request):
    # 获取父级菜单ID
    ParentId = request.GET.get('id')
    # 根据ParentID查询数据
    AccountData = Account.objects.filter(ParentMenu=ParentId)
    if len(AccountData) > 0:
        context = {
            'ListData': AccountData
        }
    else:
        context = {
        }
    return render(request, 'admin/AccountApp/AccountList.html', context=context)


def editAccount(request):
    status = 0
    msg = ''

    if request.POST:
        if not request.POST.get('accountData[username]'):
            status = 40004
            msg = '用户名不能为空！'
        elif not request.POST.get('accountData[Pwd]'):
            status = 40004
            msg = '密码不能为空！'
        elif not request.POST.get('accountData[Links]'):
            status = 40004
            msg = '链接不能为空！'
        elif not request.POST.get('accountData[Platform]'):
            status = 40004
            msg = '平台不能为空！'
        elif not request.POST.get('accountData[remarks]'):
            status = 40004
            msg = '备注不能为空！'
        else:
            userName = request.POST.get('accountData[username]')
            Pwd = request.POST.get('accountData[Pwd]')
            Links = request.POST.get('accountData[Links]')
            Platform = request.POST.get('accountData[Platform]')
            remarks = request.POST.get('accountData[remarks]')
            subDate = time.asctime(time.localtime(time.time()))
            ParentMenu = int(request.POST.get('menu'))
            itemId = int(request.POST.get('id'))

            # 新增
            if int(request.POST.get('statu')) == 0:
                addAccount = Account(userName=userName, Pwd=Pwd, Links=Links, Platform=Platform, remarks=remarks,
                                     subDate=subDate, ParentMenu_id=ParentMenu)
                addAccount.save()
                status = 20000
                msg = '数据上传成功'
            elif int(request.POST.get('statu')) == 1:
                subDateFormat = datetime.strptime(subDate, '%a %b %d %H:%M:%S %Y')
                Account.objects.filter(id=itemId).update(userName=userName, Pwd=Pwd, Links=Links, Platform=Platform,
                                                         remarks=remarks,
                                                         subDate=subDateFormat, ParentMenu_id=ParentMenu)
                status = 20000
                msg = '数据更新成功'
            elif int(request.POST.get('statu')) == 2:
                Account.objects.filter(id=itemId).delete()
                status = 20000
                msg = '数据删除成功'

    data = {
        'status': status,
        'msg': msg
    }
    dataResponse = JsonResponse(data, json_dumps_params={'ensure_ascii': False})
    dataResponse["Access-Control-Allow-Origin"] = "*"
    return dataResponse


class Accounts(View):
    """
        账号管理（增删改查）
    """

    def get(self, requests):
        accountMenuId = int(requests.GET.get('m', 0))
        pageNum = requests.GET.get('pageNum', 1)
        pageSize = requests.GET.get('pageSize', 8)

        accountList = Account.objects.all()
        if int(accountMenuId) <= 0:
            accountList = accountList
        else:
            accountList = accountList.filter(ParentMenu=accountMenuId)

        _paginator = Paginator(accountList.values(), pageSize)
        pageData = _paginator.get_page(pageNum)
        accountData = [item for item in pageData.object_list]

        for index in range(len(accountData)):
            for v in accountData[index]:
                if accountData[index][v] is None:
                    accountData[index][v] = 'none'

        print(accountData)
        data = {'code': 20000, 'msg': '数据获取成功', 'pageNum': pageNum,
                'pageSize': pageSize,
                'total': _paginator.count,
                'pages': _paginator.num_pages,
                'data': accountData
                }

        response = JsonResponse(data, json_dumps_params={'ensure_ascii': False})
        response['Access-Control-Allow-Origin'] = "*"
        return response
