from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from google_trans_new import google_translator

TOKEN = '1787783787:AAHw8Nw4aieDmt0Dub7oiEjCgCkFIvmzXvA'

target_language = 'ru'
translator = google_translator() 

def start(update, context):
    update.message.reply_text('Hi...')


def help(update, context):
    update.message.reply_text('Help...')


def translate(update, context):
    if target_language == '':
        result = 'You must specify target language'
    else:
        result = translator.translate(update.message.text, lang_tgt=target_language)
    update.message.reply_text(result)

def set_language(update, context):
    update.message.reply_text('Language set: ')

def error(update, context):
    update.message.reply_text('Something went wrong!')


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("set_language", set_language))
    dp.add_handler(MessageHandler(Filters.text, translate))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()