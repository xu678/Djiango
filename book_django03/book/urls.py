from django.urls import path
from book.views import index,goods,get,p,get_json,header,method,response,set_cookie
from django.urls import converters
from book.views import set_session,get_session,OrderView,get_cookie
from book.views import LoginView
# 转换器的导入

urlpatterns = [
    path('index/',index),
    path('<int:cat_id>/<goods_id>',goods),
    path('get/',get),
    path('post/',p),
    path('get_json/',get_json),
    path('header/',header),
    path('method/',method),
    path('get_cookie/',get_cookie),
    path('response/',response),
    path('set_cookie/',set_cookie),
    path('login163/',LoginView.as_view()),
    path('login/',OrderView.as_view()),
    path('set_session/',set_session),
    path('get_session/',get_session),
]