from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    params = {
        'title':'Hello/index',
        'msg':'お名前は？',
    }
    return render(request, 'hcMgr/index.html', params)

def form(request):
    msg = request.POST['msg']
    params = {
        'title':'Hello/Form',
        'msg':'こんにちは' + msg + 'さん',
    }
    return render(request, 'hcMgr/index.html', params)
# Create your views here.