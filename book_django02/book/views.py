from django.http import HttpResponse
import json
from django.shortcuts import render, redirect


def index(request):
    pass

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
    # response = HttpResponse("res",status=200)
    #
    # response['name'] = 'xuxuxuxu'
    #
    # return response
    # JSON --> dict
    # dict --> JSON

    info = {
        'name':'xuxuuxu',
        'address':'shunyi'
    }
    girl_friends=[
        {
            'name':'rose',
            'address':'shunyi'
        },
        {
            'name':'jack',
            'adress':'changping'
        }
    ]
    # data 返回的响应数据　一般是字典类型
    """
    safe = Turn 是表示　我们的data是字典类型
    JsonResponse 可以把字典转换为json
    
    现在给了一个非字典数据,出了问题 我们自己负责
    """
   #  response = JsonResponse(data=info)  # 安全检测机制,data不是字典要把safe变为False
#    # # response = JsonResponse(data=girl_friends,safe=False)
#    #  response['name'] = info['name']
#    #  response['address'] = info['address']
#    #  return response

    # redirect 重定向,跳到指定页面

    return redirect('http://www.baidu.com')

    # 等同于上面 JsonResponse(data=数据,safe=)
    # 没有安全机制
    # data = json.dumps(girl_friends)
    # response = HttpResponse(data)
    # return response

    # 1xx
    # 2xx  200 成功
    # 3xx
    # 4xx    请求有问题
    #   404  找不到页面 路由问题
    #   403  禁止访问   权限问题
    # 5xx
    #　HTTP status code must be an integer from 100 to 599


#####################################

"""
查询字符串
http://ip:port/path/path/?key=value&key1=value1


url 以?为分割分为2部分
? 前边为 请求路径
?  后边为 查询字符串 查询字符串 类似于字典 key=value 多个数据采用&拼接
"""





