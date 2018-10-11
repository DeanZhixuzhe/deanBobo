from django.db import models

# Create your models here.

class SpiderLog(models.Model):
	"""docstring for SpiderLog"""
	name = models.CharField(max_length=100,verbose_name='采集器名称')
	ipaddress = models.CharField(max_length=23,verbose_name='IP')
	ipproxy = models.CharField(max_length=23,verbose_name='代理IP',null=True)
	target_url = models.CharField(max_length=100,verbose_name='目标URL')
	target_ip = models.CharField(max_length=23,verbose_name='目标IP')
	action_time = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'spiber_log'
		verbose_name = '蜘蛛日志'