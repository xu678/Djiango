from django.http import HttpResponse
import json
from django.shortcuts import render

# Create your views here.
def goods(request,cat_id,goods_id):

    # print(cat_id,"------",goods_id)
    # return HttpResponse({"cat_id",cat_id,"id",goods_id})
    query_params=request.GET
    print(query_params)
    print(query_params.get("order"))
    print(query_params.getlist("order"))
    # <QueryDict: {'order':["readcount"]}>
    # QueryDict 具有字典的特性
    # 还具有　一键多值
    # <QueryDict: {'order':['readcount','commentcount'],'page':['1']}>



    return HttpResponse("骑个饭店")

def content(request):
    dict_j = request.body
    print(type(dict_j))  # bite类型需要转换成字符串
    # print(dict_j)
    dict_str = dict_j.decode()  # 字符串类型
    # print(dict_str)
    print(type(dict_str))
   # dict_json = eval(dict_str)
   #  print(dict_json)
    dict_json = json.loads(dict_str)    # 使用json模块进行解码
    print(dict_json)
    print(type(dict_json))
    # print(dict_json['name'])

    ############请求头##############
    # print(request.META)   # 获取请求头给的字典类型
    # print(type(request.META))
    # <class 'dict'>
    return HttpResponse("ok")

def method(request):
    print(request.method)  # 返回请求的方式
    return HttpResponse('method')

from django.http import HttpResponse,JsonResponse
def response(request):
    return



