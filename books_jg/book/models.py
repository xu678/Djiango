from django.db import models
"""
1. 模型类 需要继承自 models.Model
2, 定义属性
    id 系统默认会生成
    属性名 = models.类型(选项)
    
    2.1 属性名对应就是字段名
        不要使用 python,Mysql 关键字
        不要使用连续的下划线(__)
    2.2 类型 Mysql的类型
    2.3 选项 是否有默认值,是否唯一,是否为null
        CharField 必须设置 max_length
        varbose_name 主要是 admin 站点使用
3, 该变表的名称
    默认表的名称是; 子应用名_类名 都是小写
    修改表的名字
create table 'qq_user' (
    id int,
    name varchar(10) not null default
)
"""

# Create your models here.
# 准备数据列表信息的模型类
class BookInfo(models.Model):
    # 创建字段,字段类型...
    name = models.CharField(max_length=10, unique=True)
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "bookinfo"  # 修改表的名字
        verbose_name = '书籍管理'  # admin站点使用的(了解)


# 准备人物列表信息的模型
class PeopleInfo(models.Model):
    # 定义一个有序字典
    GENDER_CHOICE = (
        (1,'male'),
        (2,'female')
    )
    name = models.CharField(max_length=10, unique=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=1)
    description = models.CharField(max_length=100, null=True)
    is_delete = models.BooleanField(default=False)
    # 外键
    # 系统会自动为外键添加_id

    # 外键的级联操作
    # 主表 和 从表
    # 1 对 多
    # 书籍   对  人物

    # 主表的一条数据 如果删除了
    # 从表有关联的数据, 关联的数据怎么办呢???
    # SET_NULL
    # 抛出异常,不让删除
    # 级联删除
    # 外键约束: 人物属于哪本书
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    class Meta:
        db_table="peopleinfo"

    def __str__(self):
        return self.name