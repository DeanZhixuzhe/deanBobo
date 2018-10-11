from django.db import models

# Create your models here.
class Lottery(models.Model):
	"""docstring for Lottery"""
	name = models.CharField(max_length=100,verbose_name='名称')
	saletime = models.CharField(max_length=9,verbose_name='开售时间')
	open_frequency = models.CharField(max_length=50,verbose_name='开奖频率')
	code = models.CharField(max_length=20,verbose_name='代码',unique=True)
	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)
	class Meta:
		db_table = 'lottery'
		verbose_name = '彩种'
		

class LotteryNumber(models.Model):
	"""docstring for LotteryNumber"""
	lottery = models.ForeignKey('Lottery',on_delete=models.CASCADE,null=True)
	periods = models.CharField(max_length=13,verbose_name='期数',unique=True)
	opentime = models.DateTimeField(verbose_name='开奖时间')
	number = models.CharField(max_length=100,verbose_name='开奖号码')
	fluctuating = models.CharField(max_length=30,verbose_name='波动值')
	tencent_online_number = models.IntegerField(verbose_name='腾讯在线人数')
	ordernumber = models.IntegerField()
	create_time = models.DateTimeField(auto_now_add=True)
	class Meta:
		db_table = 'lottery_number'
		verbose_name = '开奖号'