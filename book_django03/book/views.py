from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def index(request):

    return HttpResponse('ok')

def goods(request,cat_id,goods_id):

    return HttpResponse((cat_id,goods_id))

def get(request):
    a = request.GET.get('user_name')
    b = request.GET
    alist = request.GET.getlist("user_name")

    print(a)
    print(type(a))
    print(alist)
    print(type(alist))
    print(b)
    print(type(b))
    return HttpResponse('ok')

def p(request):
    # 选择from_data表单数据
    con = request.POST
    conn = request.POST.get('a')
    co = request.POST.get('b')
    print(con)
    print(type(con))
    print(conn)
    print(type(conn))
    print(co)
    print(type(co))

    return HttpResponse('post')

def get_json(request):
    import json
    con = request.body # 接收的是一个byte类型
    # <class 'bytes'>
    print(con)
    print(type(con))
    con = json.loads(con)  # 对json数据的一个解码操作
    # <class 'dict'>
    print(con)
    print(type(con))
    # 字典的方法获取,在没数据时会报错
    # a = con['a']
    # b = con['b']
    # print(f"{a}{b}")

    # get 没数据时会返回None
    c = con.get('a')
    d = con.get('b')
    print(f"{c}{d}")

    # {
    #     "f": "xxxx",
    #     "b": "3333333"
    # }
    # None  3333333

    return HttpResponse('ok')

# 请求头的获取
def header(request):
    con = request.META
    # <class 'dict'>
    print(con)
    print(type(con))
    e = con.get("Cookie")
    print(e)
    print(type(e))

    return HttpResponse("ok")

def method(request):
    print(request.method)  # 查看请求方式
    return HttpResponse(f"{request.method}方式")


from django.http import JsonResponse,HttpResponse
def response(request):

    # response = HttpResponse('res',status=200)
    #
    # response['name'] = 'xuxuxu'
    #
    # return response

    info ={'name':'itcast','address':'shunyi'}
    girl_friends=[
        {
            'name': 'rose',
            'address': 'shunyi'
        },
        {
            'name': 'jack',
            'address': 'changping'
        }]
    # data 返回的响应数据 一般是字典类型
    # safe = True 是表示 我们的data是字典数据
    # JsonResponse 可以把字典转换为json

    # response = JsonResponse(info)  # 字典数据不会报错
    response = JsonResponse(girl_friends,safe=False)
    # 传入别的数据是需要把safe设置为False

    # return  response

    # 重定向
    return redirect('http://www.baidu.com')
    # import json
    # data = json.dumps(girl_friends)
    # # json的编码使其变成json数据
    # response = HttpResponse(data)
    # return response

def set_cookie(request):

    # 1, 获取查询字符串数据
    username = request.GET.get('username')
    password = request.GET.get('password')
    # 2, 服务器设置cookie信息
    # 通过响应对象.set_cookie方法
    response = HttpResponse('set_cookie')
    response.set_cookie('name',username,max_age=60*60)
    response.set_cookie('password',password)

    # response.delete_cookie("name")

    return  response

# from django.http import HttpResponse
def get_cookie(request):
    cookie = request.COOKIES.get("name")
    print(cookie)
    response = HttpResponse(cookie)
    response.delete_cookie('name')
    return response

def set_session(request):
    # 1 , 模拟获取用户的信息
    username = request.session.get('username')
    # 2 , 设置session信息
    # 假如 我们通过模型查询 查询到了用户的信息
    user_id = 1
    request.session['user_id'] = user_id
    request.session['username'] = username

    # clear 删除session里的数据,但是key有保留
    # request.session.clear()
    # flush 是删除所有的数据,包括key
    # request.session.flush()

    request.session.set_expiry(3600)
    return HttpResponse("set_session")

def get_session(request):
    # user_id = request.session['user_id']
    # username = request.session['username']

    user_id = request.session.get('user_id')
    username = request.session.get("username")

    # '%s',%username
    content= '{}{}'.format(user_id,username)

    return HttpResponse(content)


from django.views import View
class LoginView(View):
    def get(self,request):
        return HttpResponse("get")

    def post(self,request):
        return HttpResponse('post')

# #### ### # ########################
"""
我的订单,个人中心页面
如果登录用户 可以访问
如果未登录用户 不应该访问,应该跳转到登录页面

定义一个订单,个人中心 类视图

如果定义我有没有登录??? 我们已登录 后台站点为例

"""
from django.contrib.auth.mixins import LoginRequiredMixin

# LoginRequiredMixin 作用判断 只有登录用户才可以访问的页面

#  class OrderView(View,LoginRequiredMixin):
#  多继承是一定要注意顺序,上面这个执行as_view()时会先从View中寻找
# dispatch方法,所以没法使用到LoginRequiredMixin中的dispatch方法
# 进而没法验证登录,  __mro__可以查看继承顺序
class OrderView(LoginRequiredMixin,View):

    def get(self,request):
        #　模拟了一个标记位
        # isLogin = False
        # if not isLogin:
        #     return HttpResponse('你没有登录,跳转到整理页面中,,,,,')

        return HttpResponse('GET 我的订单页面,这个页面必须登录')

    def post(self,request):


        return HttpResponse('POST 我的订单页面,这个页面必须登录')

    """
    多继承
    python
    c++    
    """




