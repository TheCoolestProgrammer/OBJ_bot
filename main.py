import vk_api
import requests
import datetime
from vk_api.longpoll import VkLongPoll, VkEventType
now = datetime.datetime.now()
session = requests.Session()

token='d43183177e20c8307a7815180aaef13a8b56a0b7e63b06697001cae96f98248680a5dbf2e04969b047aac'


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message})

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:

            # Сообщение от пользователя
            request = event.text

            # Каменная логика ответа
            if request == "привет":
                write_msg(event.user_id, "Хай")
            elif request == "пока":
                write_msg(event.user_id, "Пока((")
            else:
                write_msg(event.user_id, "Не понял вашего ответа...")
