from bot_commands import *

updater = Updater('token')

print('server start')
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('s', start_command))

updater.start_polling()
updater.idle()
