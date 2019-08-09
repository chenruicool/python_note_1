from django.conf.urls import url
# from django.contrib.auth.views import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

from . import views

app_name = "users"

urlpatterns = [
	# 登录页面
	# url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
	url(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
	
	# 退出页面
	url(r'^logout/$', views.logout_view, name='logout'),

	# 注册页面
	url(r'^register/$', views.register, name='register'),
]

