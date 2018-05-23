from django.contrib import admin

# Register your models here.
from new import models

class Postadmin(admin.ModelAdmin):
	list_display=['name','arti','timestamp']
admin.site.register(models.userinfo)
admin.site.register(models.Name)
admin.site.register(models.Article,Postadmin)