from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
	""" 学习笔记的主页 """
	return render(request, 'learning_logs/index.html')


def topics(request):
	""" 显示所有主题 """
	topics = Topic.objects.order_by('-date_added')
	content = {'topics':topics} # key 是数据库模板的名称
	return render(request, 'learning_logs/topics.html', content)

def topic(request, topic_id):
	""" 显示所有主题 """
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-date_added') # - 表示降序
	context = {'topic':topic, 'entries':entries} # key 是数据库模板的名称
	return render(request, 'learning_logs/topic.html', context)

