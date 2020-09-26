from django.http import HttpResponse
import json
from django.shortcuts import render, redirect


def index(request):
    pass


def Cookie(request):
    response = HttpResponse('ok')
    response.set_cookie('xuxu1','python1')
    response.set_cookie("xuxu2",'python2')
    # 字典的方式获取cookie   获取不到数据会报错
    # cookie1 = request.COOKIES['xuxu1']
    # get 方式获取不到数据会返回None
    cookie1 = request.COOKIES.get('xuxu')
    # request.COOKIE返回的为字典类型
    response.delete_cookie("xuxu1")
    print(cookie1)
    return response

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
#########################################################
# session 是保存在服务器端--数据相对安全
# session需要依赖于cookie

"""
第一次请求http://127.0.0.1:8000/set_session/?uersname=xuxuxu,
我们在服务端设置session信息
服务器同时会生成一个sessionid的cookie信息
浏览器接收到这个信息之后,会把cookie数据保存起来

第二次及其之后的请求 都会携带这个sessionid,服务器会验证这个sessionid,
验证没问题会读取相关数据,实现业务逻辑

"""

def set_session(request):
    # 1, 模拟获取用户信息
    username = request.GET.get("username")

    # 2, 设置session信息
    #　假如　我们通过模型查询　查询到了用户的信息
    user_id=3
    print(username)

    request.session["user_id"] = user_id
    request.session["user_name"]=username

    # clear 删除session里的数据,但是key有保留
    # request.session.clear()
    # flush是删除所有数据,包括key
    # request.session.flush()

    # request.session.set_expiry(3600)  # 已秒为单位,默认值为两周
    return HttpResponse('set_session')

def get_session(request):
    # 字典的查询方式获取数据,没有数据是会报错,get没有数据是会返回None
    # user_id = request.session["user_id"]
    # user_name = request.session["user_name"]
    user_id = request.session.get("user_id")
    user_name = request.session.get("user_name")
    user_time = request.session.get_expiry_date()
    content = "{},{},{}".format(user_id,user_name,user_time)

    return HttpResponse(content)

####################################################
# 类视图

def login(request):
    print(request.method)
    if request.method == 'GET':
        return HttpResponse(f'{request.method}逻辑')

    else:
        return HttpResponse(f'{request.method}逻辑')


# 类视图的定义
"""
class 类视图名字(view):
    def get(self,request):
        return HttpResponse("xxxx")
    
    def http_method_lower(self,request):
        return HttpResponse("xxxx")
 
1 . 继承自view
2 . 类视图中的方法 是采用 http方法小写来区分不同的请求方式
"""
from django.views import View

class LoginView(View):

    def post(self,request):
        return HttpResponse("post  get  get")


    def get(self,request):
        return redirect('login/')



