import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

PROXY = {
    'proxy_url': 'socks5h://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def word_count(bot, update):
    user_text = update.message.text
    text = user_text.split()
    text_without_comand = text[1:]
    text_for_count = []
    if text_without_comand == []:
        update.message.reply_text(f'Для подсчета количества слов, введите их после команды через пробелы!')
    else:
        for value in text_without_comand:
            if value.isalpha():
                text_for_count.append(value)
        if text_for_count != []:
            (f'Колличество слов в этом предложении равно: {len(text_for_count)} ')
            update.message.reply_text(f'Колличество слов в этом предложении равно: {len(text_for_count)} ')
        else:
            update.message.reply_text(f'Для подсчета не принимаются слова, состоящие только из символов или цифр')
def main():
    mybot = Updater("1017943578:AAFSaBEhIBPLVK-epDLFoWpthzNNdKhkk5k", request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("wordcount", word_count))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()