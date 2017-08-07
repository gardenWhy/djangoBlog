from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'blog/index.html',context={
                        'title': '我的博客首页',
                        'welcome': '欢迎访问我的博客首页'
            })
# Create your views here.
