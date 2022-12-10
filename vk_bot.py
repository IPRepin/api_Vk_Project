from random import randrange
import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
from config import vk_group_token
import emoji


'''Создаем класс бота'''
class VkBot:
    def __init__(self, vk_group_token):
        self.vk_session = vk_api.VkApi(token=vk_group_token)

    '''Функция создания кнопок клавиатуры бота'''
    def keyboard_bot(self):
        emoji_info_user = emoji.emojize(":check_mark_button:")
        emoji_find_a_couple = emoji.emojize(":couple_with_heart_woman_man:")
        self.button_bot = VkKeyboard(one_time=False)
        name_btn = [f'{emoji_info_user}Заполнить данные о себе', f'{emoji_find_a_couple}Найти пару']
        colors_btn = [VkKeyboardColor.PRIMARY, VkKeyboardColor.NEGATIVE]
        for btn, btn_color in zip(name_btn, colors_btn):
            self.button_bot.add_button(btn, btn_color)


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
                        self.add_info_user(self.user_id)
                    elif self.text == 'найти пару':
                        self.find_a_couple()
        except Exception as ex:
            print(ex)

    '''функция ответа на сообщения'''
    def sender(self, user_id, message, keyboard=None):
        self.params = {'user_id': user_id, 'message': message, 'random_id': randrange(10 ** 7),}
        if keyboard != None:
            keyboard = self.keyboard_bot()
            self.params['keyboard'] = keyboard

        self.vk_session.method('messages.send', self.params)

    '''функция заполнения данных о пользователе (взаимодействует с модулем обращений к БД)'''
    def add_info_user(self, user_id):#логику нужно доработать
        params = {'user_ids': user_id, 'fields': {
            'sex': int,
            'city': 'title',
            'relation': int
        }, }
        self.vk_session.method('users.get', params)
        #далее запуск модуля взаимодействия с БД


    '''Функция поиска пары (взаимодействует с модулем обращений к БД)'''
    def find_a_couple(self):
        pass

    def add_black_lst(self):
        pass

    def add_favorit(self):
        pass



def main():
    vk_client = VkBot(vk_group_token)
    vk_client.reader()



if __name__ == '__main__':
    main()