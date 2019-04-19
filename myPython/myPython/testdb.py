# -*- coding: utf-8 -*-

from django.http import HttpResponse
from TestModel.models import Test


# 数据库操作---添加
def add_test_db(request):
    test1 = Test(name='runoob')
    test1.save()
    return HttpResponse("<p>数据添加成功! </p>")


# 数据库操作---获取数据
def get_test_data(request):
    response = ""
    response1 = ""

    # 通过objects这个模型管理器的all()获取所有数据行,
    list = Test.objects.all()

    # filter相当于SQL的WHERE，可设置条件过滤结果
    response2 = Test.objects.filter(id=1)

    # 获取单个对象
    response3 = Test.objects.get(id=1)

    # 限制返回的数据，相当于SQL中的OFFSET 0 LIMIT 2;
    Test.objects.order_by('name')[0:2]

    # 数据排序
    Test.objects.order_by("id")

    # 上面的方法可以连锁使用
    Test.objects.filter(name="runoob").order_by("id")

    # 输出所有数据
    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")


# 数据库操作---更新数据
def update_test_data(request):
    # 修改id=1的数据
    test = Test.objects.get(id=1)
    test.name = 'gooolbe'
    test.save()

    # 另一种方式
    # Test.objects.filter(id=1).update(name='gooble')

    # 修改所有的列
    # Test.objects.all().update(name='gooble')

    return HttpResponse("<p>修改成功</p>")


# 数据库操作---删除数据
def del_test_data(request):
    # 删除id=1的数据
    test = Test.objects.get(id=1)
    test.delete()

    # 另一种方式
    # Test.objects.filter(id=1).delete()

    # 删除所有数据
    Test.objects.all().delete()

    # return HttpResponse("<p>删除成功</p>")
