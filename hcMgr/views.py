from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    params = {
        'title':'Hello/トップページ',
        'msg':'これは、サンプルで作ったページです。',
        'goto':'next',
    }
    return render(request, 'hcMgr/index.html', params)

def next(request):
    params = {
        'title':'Hello/次へ',
        'msg':'これは、もう１つのページです。',
        'goto':'index',
    }
    return render(request, 'hcMgr/index.html', params)
# Create your views here.