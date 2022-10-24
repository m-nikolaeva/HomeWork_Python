from os.path import exists


def write_info(user, data):
    data.append(user)


def write_data(data, columns):
    with open(FILE_NAME, 'w', encoding='UTF-8') as f:
        f.write(', '.join(columns) + '\n')
        for user in data:
            f.write(', '.join(user.values()) + '\n')


def add_column(data, column, columns):
    for user in data:
        user[column] = ''
    columns.append(column)
    return data


def read_data():
    valid = exists(FILE_NAME)
    if not valid:
        return []
    with open(FILE_NAME, 'r', encoding='UTF-8') as f:
        data = f.read()
        if "\n" not in data:
            return []
        print(data.split("\n"))
        columns = data.split("\n")[0].strip().split(", ")
        data = [{columns[i]: user.strip().split(", ")[i] if user else "" for i in range(
            len(columns))} for user in data.split("\n")[1:] if user]
        return data


def get_columns(data):
    if not data:
        return ['Фамилия', 'Имя']
    columns = list(data[0].keys())
    return columns


def find_info(data):
    column = input('Введите название столбца для поиска: ')
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


def deletion_data(data):
    column = input('Введите название столбца для поиска: ')
    val = input('Введите значение для поиска: ')
    flag = False
    for user in data:
        if column not in user:
            return 'Такого столбца нет'
        if user[column] == val:
            choice = input('Чтобы удалить нажмите 2: ')
            if choice == '2':
                data.remove(user)
                flag = True
    if not flag:
        print('Такого контакта нет')


def deletion_base(data):
    choice = input(
        'Если Вы уверены, что хотите полностью очистить базу данных, нажмите 3: ')
    flag = True
    if choice == '3':
        data.clear()
        print('База данных очищена.')
    else:
        flag = False


FILE_NAME = 'data_base.csv'
