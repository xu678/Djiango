from django.http import HttpResponse
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


