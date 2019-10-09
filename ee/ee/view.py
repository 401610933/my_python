from django.shortcuts import render

def index(request):
    content = {}
    content['haha'] = "我不是一个人在战斗"
    return render(request,'index.html',content)