# from input_data import add_contact
# from contacts_op import read_contacts, find_contact


# def user_interface():
#     flag = True
#     while flag:
#         print('\nДобро пожаловать в базу данных!\n\nВыберите пункт меню для продолжения: ')
#         while True:
#             print('1 - Найти контакт')
#             print('2 - Добавить контакт')
#             print('3 - Показать все контакты')
#             print('4 - Выход')
#             choice = input()
#             if choice not in ['1', '2', '3', '4']:
#                 print('Такого пункта нет. Попробуйте еще раз')
#                 continue
#             if choice == '1':
#                 find_contact()
#                 break
#             elif choice == '2':
#                 add_contact()
#                 break
#             elif choice == '3':
#                 read_contacts()
#             else:
#                 flag = False
#                 break
            

from input_data import add_contact
from contacts_op import find_contact, read_contacts, write_contacts, get_columns


def user_interface():
    data = read_contacts()
    columns = get_columns(data)
    flag = True
    while flag:
        print('\n=====Телефонный справочник=====\n\nВыберите пункт меню для продолжения: ')
        while True:
            print('1 - Показать все контакты')
            print('2 - Добавить контакт')
            print('3 - Найти контакт')
            print('4 - Выход\n')
            choice = input()
            if choice not in ['1', '2', '3', '4']:
                print('Такого пункта нет. Попробуйте еще раз')
                continue
            if choice == '1':
                print(columns)
                print(data)
                break
            elif choice == '2':
                add_contact(data, columns)
                break
            elif choice == '3':
                find_contact(data)
            else:
                flag = False
                write_contacts(data, columns)
                break
            
