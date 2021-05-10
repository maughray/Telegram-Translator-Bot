from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from google_trans_new import google_translator
import logging


TELEGRAM_TOKEN = '1787783787:AAHw8Nw4aieDmt0Dub7oiEjCgCkFIvmzXvA'
TARGET_LANGUAGE_KEY = 'target_language'
translator = google_translator() 


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text('Hi...')


def help(update, context):
    update.message.reply_text('Help...')


def translate(update, context):
    if TARGET_LANGUAGE_KEY in context.user_data.keys():
        target_language = context.user_data[TARGET_LANGUAGE_KEY]
        result = translator.translate(update.message.text, lang_tgt=target_language)
        update.message.reply_text(result)
    else:
        update.message.reply_text('You must specify target language!')
    

def set_language(update, context): 
    language = update.message.text.split()[1]
    context.user_data[TARGET_LANGUAGE_KEY] = language # TODO: validate language
    update.message.reply_text('Language set: ' + language)


def error(update, context):
    update.message.reply_text('Something went wrong!')
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
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