from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
# from django.core.urlresolvers import reverse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.

def index(request):
	""" 学习笔记的主页 """
	return render(request, 'learning_logs/index.html')

@login_required
# login_required()的代码检查用户是否已登录，仅当用户已登录时，Django才运行topics() 的代码。
def topics(request):
	""" 显示所有主题 """
	# topics = Topic.objects.order_by('date_added')
	topics = Topic.objects.filter(owner=request.user).order_by('date_added')
	content = {'topics':topics} # key 是数据库模板的名称
	return render(request, 'learning_logs/topics.html', content)

@login_required
def topic(request, topic_id):
	""" 显示所有主题 """
	topic = Topic.objects.get(id=topic_id)
	# 确认请求的主题属于当前用户
	if topic.owner != request.user:
		raise Http404

	entries = topic.entry_set.order_by('-date_added') # - 表示降序
	context = {'topic':topic, 'entries':entries} # key 是数据库模板的名称
	return render(request, 'learning_logs/topic.html', context)

# 新主题
@login_required
def new_topic(request):
	if request.method != 'POST':
		form = TopicForm()
	else:
		form = TopicForm(request.POST)
		if form.is_valid():
			# form.save()
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			return HttpResponseRedirect(reverse('learning_logs:topics'))

	context = {'form':form}
	return render(request, 'learning_logs/new_topic.html', context)

# 新条目
@login_required
def new_entry(request, topic_id):
	topic = Topic.objects.get(id=topic_id)

	if request.method != "POST":
		form = EntryForm()
	else:
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
	context = {'topic':topic, 'form':form}
	return render(request, 'learning_logs/new_entry.html', context)

# 编辑条目
@login_required
def edit_entry(request, entry_id):
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic

	if topic.owner != request.user:
		raise Http404
		
	if request.method != "POST":
		form = EntryForm(instance=entry)
	else:
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))

	context = {'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'learning_logs/edit_entry.html', context)



