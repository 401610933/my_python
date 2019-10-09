from django.http import HttpResponse
import time
from app.models import test


# 数据库操作
def testdb(request):
    test1 = test(username='肖大爷',age='33',address='重庆市北碚区西湖山水',regtime=time.time())
    # test1 = test()
    # test1 = test(address='重庆市北碚区西湖山水')
    # test1 = test(regtime=time.time())
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")
