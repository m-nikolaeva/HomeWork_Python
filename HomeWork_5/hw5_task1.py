# Напишите программу, удаляющую из текста все слова, содержащие "абв".

input_list = 'абвгдейка, абвгдейка — Это учёба и игра, абвгдейка, абвгдейка, Азбуку детям знать пора.'.split()
text1 = 'абв'
result_list = []
for word in input_list:
    if text1 not in word:
        result_list.append(word)
print(' '.join(result_list))
