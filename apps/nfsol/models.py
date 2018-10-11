from django.db import models

# Create your models here.

class Carport(models.Model):
	"""docstring for ClassName"""
	brand = models.ForeignKey('Brand',on_delete=models.CASCADE,verbose_name='品牌')
	name = models.CharField(max_length=100,default='',verbose_name='车名',unique=True)
	engine = models.IntegerField(default=0,verbose_name='引擎')
	transmission = models.IntegerField(default=0,verbose_name='变速器')
	nitrogen = models.IntegerField(default=0,verbose_name='氮气')
	bumper = models.IntegerField(default=0,verbose_name='保险杠')
	carriage = models.IntegerField(default=0,verbose_name='车架')
	worth = models.BigIntegerField(default=0,verbose_name='价值')
	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)
	
	class Meta:
		"""docstring for Meta"""
		verbose_name = '车库'

class Parts(models.Model):
	"""docstring for ClassName"""
	level = models.SmallIntegerField(verbose_name='配件等级')
	performance = models.SmallIntegerField(verbose_name='性能值')
	upgrade = models.SmallIntegerField(verbose_name='升级配件数')
	disassembly = models.SmallIntegerField(verbose_name='拆卸器数量')

	class Meta:
		"""docstring for Meta"""
		verbose_name = '配件'

class Brand(models.Model):
	"""docstring for ClassName"""
	automanufacturer = models.ForeignKey('AutoManufacturer',on_delete=models.CASCADE,verbose_name='厂商名')
	name = models.CharField(max_length=100,default='',verbose_name='品牌名',unique=True)
	
	def __str__(self):
		return self.name

	class Meta:
		"""docstring for Meta"""
		verbose_name = '品牌'

class AutoManufacturer(models.Model):
	"""docstring for AutoManufacturer"""
	name = models.CharField(max_length=100,default='',verbose_name='汽车厂商名',unique=True)
	def __str__(self):
		return self.name
	
	class Meta:
		"""docstring for Meta"""
		verbose_name = '厂商'
			