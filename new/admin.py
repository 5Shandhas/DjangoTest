from django.contrib import admin

# Register your models here.
from new import models

class Postadmin(admin.ModelAdmin):
	list_display=['name','arti','timestamp']
class Postmao(admin.ModelAdmin):
	list_display=['name']
admin.site.register(models.userinfo)
admin.site.register(models.Name)
admin.site.register(models.Article,Postadmin)
admin.site.register(models.Mao,Postmao)