from data_base_op import write_info


def add_data(data, columns):
    print('Внесите данные нового сотрудника: ')
    flag = True
    while flag:
        user = {}
        for column in columns:
            user[column] = input(column + ': ')
        confirm = input('\nНажмите 1 для сохранения или любую клавишу для возврата в меню: ')
        if confirm == '1':
            write_info(user, data)
        flag = False

    
def input_column():
    return input('Введите название нового столбца: ')
    