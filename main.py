from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = '1787783787:AAHw8Nw4aieDmt0Dub7oiEjCgCkFIvmzXvA'

def start(update, context):
    update.message.reply_text('Hi...')


def help(update, context):
    update.message.reply_text('Help...')


def translate(update, context):
    update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Something went wrong!')


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, translate))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()