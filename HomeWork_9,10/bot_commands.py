from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from spy_log import *
from op_defenition import *


def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'/help\n'
                                f'Пример ввода для решения задач с:\n'
                                f'целыми числами: /s x+y\n'
                                f'рациональными числами: /s x/n+y/m\n'
                                f'комплексными числами: /s (x+ni)+(y+mi)')


def start_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    write_line(msg)
    update.message.reply_text(in_put_int(msg))
