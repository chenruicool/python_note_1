#! /usr/bin/env python
# coding=utf-8

# 第十八章 django 入门

# 下载 dutam 查看数据库


# 一
# 1.创建一个虚拟环境  ==> python3 -m venv ll_env
# 2.激活 ==> source ll_env/bin/activate
# 3.安装django ==> pip3 install Django
# 4.停止 ==> deactivate

# 二
# 1.开始一个项目 ==> django-admin.py startproject learning_log .
# 2.创建数据库(迁移数据库) ==>  python3 manage.py migrate
# 3.启动 ==>  python manage.py runserver
# 4.用浏览器访问 ==> http://localhost:8000/

# 三 创建应用程序
# 1.执行 startapp ==> python3 manage.py startapp learning_logs
# 2.每次在models.py中添加类后,
# 	修改数据库 ==> python3 manage.py makemigrations learning_logs
#	迁移数据库 ==> python3 manage.py migrate
# 3.每当需要修改“学习笔记”管理的数据时，都采取如下三个步骤:
# 	修改models.py;
# 	对learning_logs调用makemigrations;
# 	让Django迁移项目。

# 四 创建超级用户
# 1.执行 ==> python3 manage.py createsuperuser
# 			   ==> ll_admin 123456
# 2.Django shell ==> python3 manage.py shell

# 3.地址 http://127.0.0.1:8000/admin

# 五 创建网页
# 1.使用Django创建网页的过程通常分三个阶段:1.定义URL 2.编写视图 3.编写模板


