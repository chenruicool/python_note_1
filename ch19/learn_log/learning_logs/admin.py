from django.contrib import admin

# Register your models here.

from learning_logs.models import Topic, Entry

# 主题
admin.site.register(Topic)

# 条目
admin.site.register(Entry)

