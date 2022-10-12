# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах. 
# работает для символов, но не для цифр((

# сжатие данных
def compression_rle(txt):
    compression = ''
    i = 0
    while i < len(txt):
        count = 1
        while i + 1 < len(txt) and txt[i] == txt[i + 1]:
            count += 1
            i += 1
        compression += str(count) + txt[i]
        i += 1
    return compression


# восстановление данных
def reconstitution_rle(data):
    reconstitution = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            reconstitution += char * int(count)
            count = ''
    return reconstitution


def read_data(file):
    with open(file, 'r', encoding="UTF-8") as data:
        input_string = data.read()
    return input_string


source_text = 'HomeWork_5/source.txt'  # исходный
compression = 'HomeWork_5/compression.txt'  # сжатый
reconstitution = 'HomeWork_5/reconstitution.txt'  # восстановленный
with open(source_text, 'w', encoding="UTF-8") as data:
    data.write('adddd...hhhh,,,heee////vv')
print(read_data(source_text))
print(compression_rle(read_data(source_text)))
with open(compression, 'w', encoding="UTF-8") as data:
    data.write(compression_rle(read_data(source_text)))
print(reconstitution_rle(read_data(compression)))
with open(reconstitution, 'w', encoding="UTF-8") as data:
    data.write(reconstitution_rle(read_data(compression)))
