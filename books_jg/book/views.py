from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# from django.template import context


def index(request):
    # 准备上下文:定义在字典中的()测试数据
    context = {"title":"测试模板处理数据"}

    # 江上下文交给模板中进行处理,处理后视图响应给客户端
    return render(request, 'book/index.html',context)