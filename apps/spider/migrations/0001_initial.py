# Generated by Django 2.1.1 on 2018-09-16 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpiderLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='采集器名称')),
                ('ipaddress', models.CharField(max_length=23, verbose_name='IP')),
                ('ipproxy', models.CharField(max_length=23, null=True, verbose_name='代理IP')),
                ('target_url', models.CharField(max_length=100, verbose_name='目标URL')),
                ('target_ip', models.CharField(max_length=23, verbose_name='目标IP')),
                ('action_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '蜘蛛日志',
                'db_table': 'spiber_log',
            },
        ),
    ]