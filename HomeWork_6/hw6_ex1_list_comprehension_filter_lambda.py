# Напишите программу, удаляющую из текста все слова, содержащие "абв".


def string_edit(my_str, elem):
    return (' '.join([word for word in my_str.split() if elem not in word]))


def deletion(my_str, elem):
    return (' '.join(list(filter(lambda x: elem not in x, my_str.split()))))


input_str = 'абвгдейка, абвгдейка — это учёба и игра, абвгдейка, абвгдейка, азбуку детям знать пора.'
text1 = 'абв'
print(string_edit(input_str, text1))
print(deletion(input_str, text1))
