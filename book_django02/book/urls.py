from django.urls import path
from book.views import goods,content,method,response,index
from book.views import Cookie,set_session,get_session,login
from book.views import LoginView
from django.urls import converters
from django.urls.converters import register_converter
# 1. 定义转换器
class MobileConverter:
    # 验证数据的关键是：　正则
    regex = '1[3-9]\d{9}'

    # 验证没有问题的数据，给视图函数
    def to_python(self,value):
        return value

    # def to_url(self,values):
    # # 将匹配结果用于反向解析传值是使用（了解）
    # return value
# 2.先注册转换器，才能在第三步中使用
# converter 转换器类
#　type_name 转换器的名字
register_converter(MobileConverter,'phone')


urlpatterns = [
    path('index/',index),
    # <转换器名字：变量名>
    # 转换器会对变量数据进行　正则验证
    path('<int:cat_id>/<phone:goods_id>/',goods),
    path('content/',content),
    path('method/',method),
    path('response/',response),
    path('Cookie/',Cookie),
    path('set_session',set_session),
    path('get_session',get_session),
    path('login',login),
    path('loginview',LoginView.as_view())
]