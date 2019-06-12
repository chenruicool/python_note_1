#! /usr/bin/env python
# coding=utf-8

# 第十七章 使用api


# 安装 requests
# pip3 install --user requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

import requests
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
# print(r.status_code)

response_dict = r.json()
# print(response_dict.keys())

# 仓库数量
print("Total repositories:", response_dict['total_count'])

# 全部仓库
repo_dicts = response_dict['items']
print("Repositories returned", len(repo_dicts))

if False:
	# 第一个仓库
	repo_dict = repo_dicts[0]

	# for key in sorted(repo_dict.keys()):
	for key, value in repo_dict.items():
		print(key, value)


my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

names, stars = [], []
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	stars.append(repo_dict['stargazers_count'])

my_style = LS('#333366', base_style=LCS)
# chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart = pygal.Bar(my_config, style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Project On Github'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')



