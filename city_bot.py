import json
import random
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

with open('cities.json', 'r', encoding='utf-8') as file:
    file_cities = json.load(file)

city_and_obl = list(set(map(lambda x: x['city'], file_cities)))
session_dict = {}

class BaseGame():
    def __init__(self, user_id, cities, session_dict, user_step):
        self.user_id = user_id
        self.session_dict = session_dict
        self.cities = cities
        self.user_step = user_step

    def session(self):
        if self.user_id in self.session_dict:
            return self.session_dict
        else:
            self.session_dict[self.user_id] = [self.cities.copy(), []]
            return self.session_dict

    def check_letter(self):
        except_letters = 'ыьъ'
        letter = self.user_step[-1]
        if letter in except_letters:
            letter = self.user_step[-2]
        return letter

    @property
    def step(self):
        city_dict = self.session()
        if self.user_step in city_dict[self.user_id][1]:
            print('Этот город уже был!')
            return 'Этот город уже был!'
        else:
            city_dict[self.user_id][1].append(self.user_step)
            try:
                city_dict[self.user_id][0].remove(self.user_step)
                words = []
                letter = self.check_letter()
                words += [city_dict[self.user_id][0].index(city) for city in city_dict[self.user_id][0] if city[0].lower() == letter]
                index_city = random.choice(words)
                answer = city_dict[self.user_id][0][index_city]
                city_dict[self.user_id][1].append(city_dict[self.user_id][0].pop(index_city))
                print(answer)
                return answer
            except ValueError:
                print('Такого города несуществует!')
                return 'Такого города несуществует!'

    def session_stop(self):
        del self.session_dict[self.user_id]


def cities_game(bot, update):
    user_text = update.message.text
    text = user_text.split()
    user_id = update.message.chat.id
    user_step = text[1]
    if user_step.isalpha():
        game1 = BaseGame(user_id, city_and_obl, session_dict, user_step)
        update.message.reply_text(game1.step)
    else:
        print('Название города должно состоять только из букв')
        update.message.reply_text('Название города должно состоять только из букв')


def main():
    mybot = Updater("1017943578:AAFSaBEhIBPLVK-epDLFoWpthzNNdKhkk5k", request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("cities", cities_game))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
