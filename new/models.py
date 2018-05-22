from django.db import models

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
	def __str__(self):
		return self.name
class Article(models.Model):
	arti=models.TextField()
