# Напишите программу, удаляющую из текста все слова, содержащие "абв".

input_list = 'абвгдейка, абвгдейка — это учёба и игра, абвгдейка, абвгдейка, азбуку детям знать пора.'.split()
text1 = 'абв'
result_list = []
for word in input_list:
    if text1 not in word:
        result_list.append(word)
print(' '.join(result_list))

