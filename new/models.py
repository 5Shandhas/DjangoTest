from django.db import models

# 使用时间字段
from datetime import datetime
# Create your models here.
class Name(models.Model):
	name=models.CharField(max_length=100)

	def __str__(self):
		return self.name
#用户信息表
class userinfo(models.Model):
	useid=models.AutoField(primary_key=True)
	name=models.CharField(max_length=50)
	email=models.EmailField(db_index=True)
	memo=models.TextField()
	img=models.ImageField(upload_to='upload')
	# user_type=models.ForeignKey("UserType",on_delete=models.CASCADE)
	gende=models.IntegerField(choices=((0,'男'),(1,'女'),),default=0)
	Dtime=models.DateTimeField(default=datetime.now,verbose_name="添加时间")
	def __str__(self):
		return self.name
class Article(models.Model):
	name=models.CharField(max_length=100,default=' ')
	arti=models.TextField()
	timestamp=models.DateTimeField(default=datetime.now,verbose_name="添加时间")
	def __str__(self):
		return self.name

class Mao(models.Model):
	name=models.CharField(max_length=100,default=' ')
	arti=models.TextField()
	def __str__(self):
		return self.name