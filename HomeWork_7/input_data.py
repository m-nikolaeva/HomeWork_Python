from contacts_op import write_contact


def add_contact(data, columns):
    print('Внесите данные нового контакта: ')
    flag = True
    while flag:
        user = {}
        for column in columns:
            user[column] = input(column + ': ')
        confirm = input('\nЧтобы сохранить данные, нажмите 5: ')
        if confirm == '5':
            write_contact(user, data)
        flag = False

    
