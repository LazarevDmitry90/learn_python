from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def main():
    updater = Updater("363115236:AAE6LLQk0iPT2ccju-entKTJiQvtXGg2Few")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("help", help_user))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    dp.add_error_handler(show_error)
    updater.start_polling()
    updater.idle()

def show_error(bot, update, error):
    print(error)

def greet_user(bot, update):
    print('Вызван /start')
    print(update)
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')

def help_user(bot, update):
    bot.sendMessage(update.message.chat_id, text='Даже не проси о помощи!')

def talk_to_me(bot, update):
    print(update.message.text)
    bot.sendMessage(update.message.chat_id, update.message.text + ', я не повторяю, я же сказал!')

main()