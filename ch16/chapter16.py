#! /usr/bin/env python
# coding=utf-8

# 第十六章 下载数据

# 安装 pygal_maps_world
# 命令 pip3 install pygal_maps_world 

import csv
from datetime import datetime
from matplotlib import pyplot as plt
import json
# from pygal.i18n import COUNTRIES # 不能用了
import pygal.maps.world
COUNTRIES = pygal.maps.world.COUNTRIES

if True:
	filename = 'sitka_weather_07-2014.csv'
	with open(filename) as f:
		reader = csv.reader(f)
		header_row = next(reader)
		# print(header_row)
		for index, column_header in enumerate(header_row):
			print(index, column_header)

		dates, highs, lows = [], [], []
		for row in reader:
			current_date = datetime.strptime(row[0], "%Y-%m-%d")
			dates.append(current_date)

			high = int(row[1])
			highs.append(high)

			low = int(row[3])
			lows.append(low)
		print(highs)

		# 根据数据绘制图形
		plt.title("Daily high and low temperatures - 2014", fontsize=24)
		fig = plt.figure(dpi=128, figsize=(10, 6))
		plt.plot(dates, highs, c='red', alpha=0.5)
		plt.plot(dates, lows, c='blue', alpha=0.5)
		plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
		# plt.plot(highs, c='red')
		plt.title("Daily high temperatures, July 2014", fontsize=24)
		plt.xlabel('', fontsize=16)
		fig.autofmt_xdate()
		plt.ylabel("Temperature (F)", fontsize=16)
		plt.tick_params(axis='both', which='major', labelsize=16)
		plt.show()

##############################################################################
# 制作世界人口地图:JSON格式
def get_country_code(country_name):
	for code, name in COUNTRIES.items():
		if name == country_name:
			return code
	return None

##############################################################################
def getPopulations():
	cc_populations = {}
	filename = 'population_data.json'

	with open(filename) as f:
		pop_data = json.load(f)

	for pop_dict in pop_data:
		if pop_dict['Year'] == '2010':
			country_name = pop_dict['Country Name']
			population = int(float((pop_dict['Value'])))
			# print(country_name + ": " + str(population))
			code = get_country_code(country_name)
			if code:
				cc_populations[code] = population

	return cc_populations

##############################################################################
def createAmericanMaps():
	# wm = pygal.Worldmap()
	wm = pygal.maps.world.World()
	wm.title = 'North, Central, and South America'

	wm.add('North America', ['ca', 'mx', 'us'])
	wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
	wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

	wm.render_to_file('americas.svg')

##############################################################################
def createWorldMaps(cc_populations):
	cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
	for cc, pop in cc_populations.items():
		if pop < 10000*1000:
			cc_pops_1[cc] = pop
		elif pop <10000*10000:
			cc_pops_2[cc] = pop
		else:
			cc_pops_3[cc] = pop

	wm = pygal.maps.world.World()
	wm.title = 'World Population in 2010'
	# wm.add('2010', cc_populations)
	wm.add('0-10m', cc_pops_1)
	wm.add('10m-1bm', cc_pops_2)
	wm.add('>1bm', cc_pops_3)
	wm.render_to_file('world_population.svg')

##############################################################################

if False:
	createAmericanMaps()

if False:
	cc_populations = getPopulations()
	createWorldMaps(cc_populations)

