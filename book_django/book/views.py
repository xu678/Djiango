# 导入HttpResponse模块
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.



# 定义视图函数
def index(request):
    # return HttpResponse('ok')

    # 准备上下文：定义在字典中（测试数据）
    context = {"title":"测试模板数据"}

    # 将上下文交给模板中进行处理，处理后视图响应给客户断端
    return render(request,"book/index.html",context)