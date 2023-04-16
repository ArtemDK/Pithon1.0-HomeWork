# ПАЛИНДРОМЫ
# а) на вход подается слово - проверить, является ли оно палиндромом
import re

word = 'Леша на полке клопа нашел.,'
word_lower = word.lower()
word_list = re.sub(r'[.,!?\'\" ]', '', word_lower)
print(word_list)
middle = int(len(word_list) / 2)
i = 0
increment = 1
flag = 1

for i in range(middle):
    if word_list[i] == word_list[i - increment]:
        print(word_list[i], word_list[i - increment])
        increment += 2
    else:
        flag = 0
        break
if flag == 1:
    print('Фраза -  Палиандром')
else:
    print('Фраза -  НЕ Палиандром')
