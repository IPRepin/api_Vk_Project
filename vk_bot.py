import json
import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
from config import vk_group_token


'''Создаем класс бота'''
class VkBot:
    def __init__(self, vk_group_token):
        self.vk_session = vk_api.VkApi(token=vk_group_token)

    def keyboard_bot(self):
        self.batton_bot = VkKeyboard(one_time=True)
        self.name_btn = ['Кнопка 1', 'Кнопка 2', 'Кнопка 1',]
        self.colors_btn = [VkKeyboardColor.PRIMARY, VkKeyboardColor.NEGATIVE, VkKeyboardColor.POSITIVE]
        for btn, btn_color in zip(self.name_btn, self.colors_btn):
            self.batton_bot(btn, btn_color)


    '''Функция по распознованию сообщений и user_id. '''
    def reader(self):
        try:
            for self.event in VkLongPoll(self.vk_session).listen():
                if self.event.type == VkEventType.MESSAGE_NEW and self.event.to_me:
                    self.user_id = self.event.user_id
                    self.text = self.event.text.lower()
                    if self.text == 'старт':
                        self.sender(self.user_id, "Привет я просто бот!!!")

        except Exception as ex:
            print(ex)

    '''функция ответа на сообщения'''
    def sender(self, user_id, message, keyboard=None):
        self.params = {'user_id': user_id, 'message': message, 'random_id': 0}
        if keyboard != None:
            self.params['keyboard'] = keyboard.keyboard_bot()
        else:
            self.params = self.params
        self.vk_session.method('messages.send', self.params)






def main():
    vk_client = VkBot(vk_group_token)
    vk_client.reader()



if __name__ == '__main__':
    main()