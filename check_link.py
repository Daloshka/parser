# Рабочий скрипт для вставки ссылком без повторений. Для запуска поместить Название предмета >
# перейти на следующую строчку и написать ссылку и поставить \n для перехода на следующую строку


with open("links_beta.txt") as f:
    content = f.readlines()
	# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] # словарь с названием и ссылкой
print(content)

with open("links.txt") as f2:
    content2 = f2.readlines()
	# you may also want to remove whitespace characters like `\n` at the end of each line
content2 = [x.strip() for x in content2] # словарь с названием и ссылкой
print(content2)

text_file = open('links.txt' , 'a')
i = 1
print(content[0::2])
print(content[0::2])

while i<len(content):   # потел целый час, потому что i = i + 2 указал не в том месте
	for a in content[0::2]:
		if a in content2[0::2]:
			i = i + 2
			pass
		else:
			text_file.write(f"{content[i-1]}\n{content[i]}\n")
			i = i + 2
	



f.close()
f2.close()
text_file.close()