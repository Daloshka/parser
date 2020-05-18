import json
import requests


def toFixed(numObj, digits=0):  # функция для уменьшения кол-ва знаков после точки в дробных числах
    return f"{numObj:.{digits}f}"

with open("links.txt") as f:
    content = f.readlines()
	# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] # словарь с названием и ссылкой
#print(content)

i = 1
profit_list = []
profit_name_list = []
while i<len(content):  # цикл для считывания информации из блокнотаb
	r = requests.get(content[i])
	json_page = json.loads(r.text) # string to json
	sell = json_page['lowest_sell_order']  # цена продажи, нужно справа отступить два символа и поставить запятую
	buy = json_page['highest_buy_order'] # цена продажи, нужно справа отступить два символа и поставить запятую
	sell_count = json_page['sell_order_count'] # цена продажи
	buy_count = json_page['buy_order_count'] # цена покупки
	profit = float(sell) * 0.87 - float(buy) # Вычисление профита
	info = 'Цена продажи: ' + sell[0:-2] + ',' + sell[-2:] + ' руб и ' + sell_count + ' шт\n' + 'Цена покупки: ' + buy[0:-2] + ',' + buy[-2:] + ' руб и ' + buy_count + ' шт'
	profit = (float(sell) * 0.86 - float(buy))/100 # высчитываю профит но с длинной дробной частью
	profit = toFixed(profit, 2) # отрезаю длинную дробную часть
	if float(profit)>0:
		profit_name_list.append(content[i-1])	
		profit_list.append(profit)
	final_profit_list = dict(zip(profit_name_list, profit_list))
	print()
	print(content[i-1])
	print('Профит ' + profit + ' руб')
	print(info)
	i = i + 2

print()
if len(final_profit_list)>0:
	print(final_profit_list)
else:
	print('\nНет профитных предметов')

f.close() # закрытие блокн





	

