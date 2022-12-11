if self.text in ['старт', 'начать', 'start']:
    self.sender(self.user_id, "Привет я просто бот!!!")
elif self.text == 'заполнить данные о себе':
    self.add_info_user(self)
elif self.text == 'найти пару':
    self.find_a_couple()


