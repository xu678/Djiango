# 导入HttpResponse模块
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.



# 定义视图函数
def index(request):
    return HttpResponse('ok')
