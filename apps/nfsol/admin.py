from django.contrib import admin

# Register your models here.

from . import models

class AutoManufacturerAdmin(admin.ModelAdmin):
	"""docstring for AutoManufacturer"""
	list_display = ['id','name']

class BrandAdmin(admin.ModelAdmin):
	def get_automanufacturer_name(self,obj):
		return obj.automanufacturer.name
	get_automanufacturer_name.short_description = '厂商名称'
	list_display = ['id','name','get_automanufacturer_name']
		
class CarportAdmin(admin.ModelAdmin):
	"""docstring for CarportAdmin"""
	#self代表CarportAdmin类本身，obj代表Models中Carport类对象
	#这个函数调用Carport类的engine、transmission、nitrogen属性进行计算，得到平均值
	def get_average(self,obj):
		return int((obj.engine+obj.transmission+obj.nitrogen)/3)
	get_average.short_description = '平均能力值'

	def worth_thousands(self,obj):
		return format(obj.worth,',')
	worth_thousands.short_description = '价值'

	list_per_page = 200;
	list_display = ['name','brand','get_average','engine','transmission','nitrogen','bumper','carriage','worth_thousands']
	list_filter = ['brand']
	search_fields = ['name']
	
	

class PartsAdmin(admin.ModelAdmin):
	"""docstring for PartsAdminadmin.ModelAdmin"""
	list_display = ['level','performance','upgrade','disassembly']
	
admin.site.register(models.AutoManufacturer,AutoManufacturerAdmin)
admin.site.register(models.Brand,BrandAdmin)
admin.site.register(models.Carport,CarportAdmin)
admin.site.register(models.Parts,PartsAdmin)
