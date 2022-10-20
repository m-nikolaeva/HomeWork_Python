from os.path import exists


def write_contact(user, data):
    data.append(user)


def write_contacts(data, columns):
    with open(FILE_NAME, 'w', encoding='UTF-8') as f:
        f.write(', '.join(columns) + '\n')
        for user in data:
            f.write(', '.join(user.values()) + '\n')


def read_contacts():
    valid = exists(FILE_NAME)
    if not valid:
        return []
    with open(FILE_NAME, 'r', encoding='UTF-8') as f:
        data = f.read()
        columns = data[0].strip().split(', ')
        data = [{columns[i]: user.strip().split(', ')[i] for i in range(len(columns))} for user in data.split()[1:]]
        return data


def get_columns(data):
    if not data:
        return ['Фамилия', 'Имя', 'Номер телефона', 'Примечание']
    columns = data[0].keys()
    return columns


def find_contact(data):
    column = input('В каком столбце будем искать? Введите название столбца (с заглавной буквы): ')
    val = input('Введите значение для поиска: ')
    flag = False
    for user in data:
        if column not in user:
            return 'Такого столбца нет.'
        if user[column] == val:
            print(user)
            flag = True
    if not flag:
        print('Данные не найдены.')


FILE_NAME = 'phonebook.csv'
