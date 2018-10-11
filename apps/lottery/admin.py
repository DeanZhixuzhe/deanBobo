from django.contrib import admin

# Register your models here.

from . import models

class LotteryAdmin(admin.ModelAdmin):
	list_per_page = 30	#每页显示数量
	actions_on_top = True	#
	list_display = ['id','name','saletime','open_frequency','code','create_time']	#要显示的字段
	list_display_links = ['name','code']
	# list_editable = ['name']
	# list_filter = ['name']	#右侧过滤器
	search_fields = ['name','code']	#搜索字段
		
class LotteryNumberAdmin(admin.ModelAdmin):
	list_per_page = 1400
	list_display = ['id','periods','opentime','number']
		
admin.site.register(models.Lottery,LotteryAdmin)
admin.site.register(models.LotteryNumber,LotteryNumberAdmin)
# admin.site.register()