from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
  param = {
    'title':'Hello/Index',
    'msg':'お名前は？',
  }
  return render(request, 'hello/index.html', param)

def form(request):
  msg = request.POST['msg']
  param = {
    'title':'Hello/Form',
    'msg':'こんにちは ' + msg +' さん！',
  }
  return render(request, 'hello/index.html', param)