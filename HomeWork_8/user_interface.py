from input_data import add_data, input_column
from data_base_op import find_info, read_data, add_column, write_data, get_columns, deletion_data, deletion_base


def user_interface():
    data = read_data()
    columns = get_columns(data)
    flag = True
    while flag:
        print('\nДобро пожаловать в базу данных!\n\nВыберите пункт меню для продолжения: ')
        while True:
            print('1 - Найти данные сотрудника')
            print('2 - Добавить данные сотрудника')
            print('3 - Показать данные всех сотрудников')
            print('4 - Добавить столбец')
            print('5 - Удалить данные сотрудника')
            print('6 - Очистить базу данных')
            print('7 - Выход')
            choice = input()
            if choice not in ['1', '2', '3', '4', '5', '6', '7']:
                print('Такого пункта нет. Попробуйте еще раз')
                continue
            if choice == '1':
                find_info(data)
                break
            elif choice == '2':
                add_data(data, columns)
                break
            elif choice == '3':
                print(columns)
                print(data)
            elif choice == '4':
                column = input_column()
                data = add_column(data, column, columns)
            elif choice == '5':
                deletion_data(data)
                print(data)
            elif choice == '6':
                deletion_base(data)
            else:
                flag = False
                write_data(data, columns)
                break
