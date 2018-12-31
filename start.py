import ezprox
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(bot, update):
    keyboard = [[InlineKeyboardButton("Send me proxies", callback_data='send_proxies'),
                 InlineKeyboardButton("I want to donate <3", callback_data='donate')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Hello! and welcome to EZproxy bot by Alireza Shamsaei.\nChoose an option:', reply_markup=reply_markup)


def button(bot, update):
    query = update.callback_query
    if query.data == 'send_proxies':
        bot.edit_message_text(text=ezprox.gimmeprox(),
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id)
    elif query.data == 'donate':
        bot.edit_message_text(text="Thank you!\nhttps://www.payping.ir/alirezashamsaei",
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id)

    # bot.edit_message_text(text="Selected option: {}".format(query.data),
    #                       chat_id=query.message.chat_id,
    #                       message_id=query.message.message_id)
    #


def help(bot, update):
    update.message.reply_text("Use /start to test this bot.")


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater("638953734:AAHXpyMf098lNwHa1ZrzAaPy9K57ZfkTry0")

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
