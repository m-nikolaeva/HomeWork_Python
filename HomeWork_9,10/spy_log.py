from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from datetime import datetime


def log(update: Update, context: CallbackContext):
    with open('log_file.csv', 'a', encoding='utf-8') as file:
        file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}, /'
                   f'{datetime.now().strftime("%d/%m/%y %H:%M")}\n')


def write_line(a):
    print(a)
    return a


def in_txt(a):
    return input(a)
