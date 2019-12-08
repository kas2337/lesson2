import json
import random

with open('cities.json', 'r', encoding='utf-8') as file:
    file_cities = json.load(file)

cities = list(set(map(lambda x: x['city'], file_cities)))
user_id = 2345679
user_step = 'Москва'
session_dict = {}

class BaseGame():
    def __init__(self, user_id, cities, session_dict, user_step):
        self.user_id = user_id
        self.cities = cities
        self.session_dict = session_dict
        self.user_step = user_step
    
    def session(self):
        cities_start = self.cities.copy()
        cities_pop = []
        self.session_dict[user_id] = [cities_start, cities_pop]
        return self.session_dict

    def check_letter(self):
        except_letters = 'ыьъ'
        letter = self.user_step[-1]
        if letter in except_letters:
            letter = self.user_step[-2]
        return letter
       
    def step(self):
        city_dict = self.session()
        city_start, city_pop = city_dict[self.user_id]
        if user_step in city_pop:
            print('Этот город уже был!')
        else:
            city_pop.append(self.user_step)
            try:
                city_start.remove(self.user_step)
                words = []
                letter = self.check_letter()
                words += [city_start.index(city) for city in city_start if city[0].lower() == letter]
                index_city = random.choice(words)
                answer = city_start[index_city]
                city_pop = city_start.pop(index_city)
                print(answer)
            except ValueError:
                print('Такого города несуществует!')

    def session_stop(self):
        del session_dict[user_id]
 
if user_step.isalpha():    
    game1 = BaseGame(user_id, cities, session_dict, user_step)
    game1.step()
else:
    print('Название города должно состоять только из букв')
    
    
