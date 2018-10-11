from django.urls import path
from . import views

app_name = 'index'

urlpatterns = [
	path('',views.index,name='index'),
	path('login/',views.login,name='login'),
	path('txffc/',views.txffc,name='txffc'),
	path('cqssc/',views.cqssc,name='cqssc'),
	path('fankui/',views.fankui,name='fankui'),
	path('caiji/',views.caiji,name='caiji')
]