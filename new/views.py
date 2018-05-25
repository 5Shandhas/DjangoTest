# coding:utf-8
# 对request的render函数
from django.shortcuts import render
# 直接str响应
from django.http import HttpResponse,Http404

from django.views.generic import View

# 从模板models中获取数据
from new import models
# 使用View类
class HomeView(View):
	def get(self,request):
		return render(request, " ")
# 这是一个HttpResponse的应用
# def index(request):
# 	return HttpResponse("Make greate deal")
#这是一个request方法的应用,可以看做需要参数的网页
def add(request):
	#a和b均为获取的参数
	a=request.GET['a']
	b=request.GET['b']
	c=int(a)+int(b)
	return HttpResponse(str(c))
# 主页
def mainpage(request):
	return HttpResponse("<h1  align='center'>Welcome to the Mainpage</h1></br><a href='admin' align='center'>Admin</a></br><a href='index' align='center'>index</a>")
# 文章列表
def index(request):
	get_result=models.Article.objects.all()
	return render(request, 'index.html',{'get_result':get_result})
def index1(request):
	return render(request,'index1.html')