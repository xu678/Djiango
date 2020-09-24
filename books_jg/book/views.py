from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# from django.template import context

#
# from book.models import BookInfo
# book = BookInfo.objects.all(id__in=(1,2))

#
# def index(request):
#     # 准备上下文:定义在字典中的()测试数据
#     context = {"title":"测试模板处理数据"}
#
#     # 江上下文交给模板中进行处理,处理后视图响应给客户端
#     return render(request, 'book/index.html',context)


######################数据的添加###########################
# 方法一
from book.models import BookInfo,PeopleInfo
book = BookInfo(
    name = 'python入门',
    pub_date='2010-1-1'
)
book.save()  # 像事件的提交

# 方法二
PeopleInfo.objects.create(
    name = "itheima",
    book = book)

########################数据的修改#########################
# 方法一
person = PeopleInfo.objects.get(name="itheima")
person.name = "itcast"
person.save()

# 方法二
PeopleInfo.objects.filter(name="itcast").update(name="传智博客")
# 会返回影响的行数

##########################数据的删除######################
# 方法一  模型类对象 delete
person = PeopleInfo.objects.get(name="传智播客")
person.delete()

# 方法二  模型类.objects.filter().delete()
BookInfo.objects.get(name="python入门").delete()
BookInfo.objects.filter(name="python入门").delete()

###############################数据的查询#######################

# get查询单一结果,如果不存在会抛出模型类.DoesNoExist异常
try:
    book = BookInfo.objects.get(id=1)
except BookInfo.DoesNotExist:
    print("你所查询的数据不存在")

# all 查询多个结果
BookInfo.objects.all()
PeopleInfo.objects.all()

# count 查询结果数量.
PeopleInfo.objects.all().count()
PeopleInfo.objects.count()  # 和上面的结果一样


#####################过滤查询########################
# 实现SQL中的where功能,包括
# filter过滤出多个结果
# exclude排除掉符合条件剩下的结果
# get过滤单一结果

# 模型名.objects.filter(属性名__运算=值)   获取n个结果
# 模型类名.objects.exclude(属性名__运算符=值)  获取n个值
# 模型类名.objects.get(属性名__运算符=值)  获取一个结果或是异常

# 查询编号为1的图书
BookInfo.objects.get(id__exact=1) # 完整形式
BookInfo.objects.get(id=1)   # 简写形式
BookInfo.objects.filter(id=1)  # 返回的列表
BookInfo.objects.get(pk=1)  # primary key 主键
BookInfo.objects.filter(pk=1)
# get获取数据时如果没有查询到抛出BookInfo.DoesNotExist异常
# filter没有获取到数据会返回一个空的列表


# 查询书名包含'湖'的图书
BookInfo.objects.filter(name__contains="湖")


# 查询书名以'部'结尾的图书
BookInfo.objects.filter(name__endswith="部")

# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)

# 查询编号为1或3或5的图书
BookInfo.objects.filter(id__in=(1,3,5))
BookInfo.objects.filter(pk__in=(1,3,5))

# 查询编号大于3的图书
# 大于  gt    great 大
# 大于等于  gte  e  equal

# 小于 lt    litte
# 小于等于 lte
BookInfo.objects.filter(id__gt=3)


# 查询编号不等于3的书籍
BookInfo.objects.exclude(id=3)

# 查询1980年发表的图书
BookInfo.objects.filter(pub_date__year="1980")

# 查询1990年1月1日后发表的图书
BookInfo.objects.filter(pub_date__gt="1990-1-1")

# 错误的是
#BookInfo.objects.filter(pub_date__gt="199011")
from django.db.models import F

# 使用: 2个属性的比较
# 语法形式; 以filter为例 模型类名.objects.filter(属性名__运算符=F("第二个属性名"))

# 查询阅读量大于等于评论量的书

BookInfo.objects.filter(readcount__gte=F("conmmentcount"))

###################################################

# 并且查询
# 查询阅读量大于20,并且编号小于3的图书.
BookInfo.objects.filter(readcount__gt=20).filter(id__lt=3)
# 或者
BookInfo.objects.filter(readcount__gt=20,id__lt=3)


# 或者查询
# 查询阅读量大于20,或者编号小于3的图示
from django.db.models import Q

# 或者语法: 模型类名.objects.filter(Q(属性名__运算符=值)|Q(属性名__预算符=值|,,,,))
# 并且语法: 模型类名.objects.filter(Q(属性名__运算符=值)&Q(属性名__运算符=值))
# not 非语法：　模型类名．objects.filter(~Q(属性名__运算符=值))
#
BookInfo.objects.filter(Q(readcount__gt=20)|Q(id__lt=3))


# 查询编号不等于３的书籍
BookInfo.objects.exclude(id=3)

BookInfo.objects.filter(~Q(id=3))


# 查询图书的总阅读量
from django.db.models import Sum
BookInfo.objects.aggregate(Sum("readcount"))
# aggregate的返回值是一个字典类型 {"属性名＿＿聚合类小写",值}
# 查询图书总数
BookInfo.objects.count()
# count函数返回的是一个数字


#    排序
BookInfo.objects.all().order_by("readcount")

#    2个表的级联操作

# 查询书籍为1的所有人物信息
PeopleInfo.objects.filter(book=1)

# 获取ｉｄ为１的书籍
book = BookInfo.objects.get(id=1)
book.peopleinfo_set.all()

# 查询人物为1的书籍信息
person=PeopleInfo.objects.get(id=1)
person.book.name
person.readcount

#   关联过滤查询
# 语法形式
#  查询１的数据，条件为ｎ
# 模型类名.objects.(关联模型类名小写＿字段名＿预算符＝值)


# 查询图书，要求图书人物为"郭靖"
BookInfo.objects.filter(peopleinfo__name__exact="郭靖")


# 查询图书，要求图书中人物的描述包含"八"
BookInfo.objects.filter(peopleinfo__description__contains="八")

# 查询书名为“天龙八部”的所有人物
PeopleInfo.objects.filter(book__name="天龙八部")


# 查询图书阅读量大于30的所有人物
PeopleInfo.objects.filter(book__readcount__gt=30)



