import json
import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
from config import vk_group_token


'''Создаем класс бота'''
class VkBot:
    def __init__(self, vk_group_token):
        self.vk_session = vk_api.VkApi(token=vk_group_token)

    '''Функция создания кнопок клавиатуры бота'''
    def keyboard_bot(self):
        self.batton_bot = VkKeyboard(one_time=False)
        name_btn = ['Заполнить данные о себе', 'Найти пару']
        colors_btn = [VkKeyboardColor.PRIMARY, VkKeyboardColor.NEGATIVE]
        for btn, btn_color in zip(name_btn, colors_btn):
            self.batton_bot.add_button(btn, btn_color)


    '''Функция по распознованию сообщений и user_id. '''
    def reader(self):
        try:
            for self.event in VkLongPoll(self.vk_session).listen():
                if self.event.type == VkEventType.MESSAGE_NEW and self.event.to_me:
                    self.user_id = self.event.user_id
                    self.text = self.event.text.lower()
                    if self.text in ['старт', 'начать', 'start']:
                        self.sender(self.user_id, "Привет я просто бот!!!")
                    elif self.text == 'заполнить данные о себе':
                        self.add_info_user()
                    elif self.text == 'найти пару':
                        self.find_a_couple()
        except Exception as ex:
            print(ex)

    '''функция ответа на сообщения'''
    def sender(self, user_id, message, keyboard=None):
        self.params = {'user_id': user_id, 'message': message, 'random_id': 0}
        if keyboard != None:
            keyboard = self.keyboard_bot()
            self.params['keyboard'] = keyboard
        else:
            self.params = self.params
        self.vk_session.method('messages.send', self.params)

    '''функция заполнения данных о пользователе (взаимодействует с модулем обращений к БД)'''
    def add_info_user(self):#логику нужно доработать
        while True:
            self.name = self.sender(self.user_id, 'Ваше имя: ')
            if self.text != '':
                self.lost_name = self.sender(self.user_id, 'Ваша фамилия: ')
                if self.text != '':
                    break
            else:
                print('Ведите данные повторно')
        while True:
            self.gender = self.sender(self.user_id, 'Укажите ваш пол: ')
            if self.text == 'женьщина' or 'мужчина' or 'не определился':
                break
            else:
                print('Ведите данные повторно')
        while True:
            self.age = self.sender(self.user_id, 'Ваш возраст(цифрой): ')
            if self.age.isdigit():
                break
            else:
                print('Ведите данные повторно')
        while True:
            self.city = self.sender(self.user_id, 'Ваше имя: ')
            if self.text != '':
                break
            else:
                print('Ведите данные повторно')




    '''Функция поиска пары (взаимодействует с модулем обращений к БД)'''
    def find_a_couple(self):
        pass




def main():
    vk_client = VkBot(vk_group_token)
    vk_client.reader()



if __name__ == '__main__':
    main()