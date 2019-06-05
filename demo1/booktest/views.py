# from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInfo,HeroInfo

# Create your views here.
def index(req):
    return HttpResponse("这里是首页")

def list(req):
    books=BookInfo.objects.all()
    return HttpResponse("这里是列表页")

def detail(req,id):
    book=BookInfo.objects.get()
    return HttpResponse("这里是详情页%s"%(id))