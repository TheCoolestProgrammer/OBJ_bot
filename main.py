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
    if not event.from_chat:
        d =datetime.datetime.now().hour
        if datetime.datetime.today().weekday() == 2 and (d ==14 or d == 18 or d ==20):
            write_msg(event.user_id, "завтра ОБЖ! всем принести тетрадки, иначе не будем смотреть видео, а будем писать в тетрадках!")
        # Если пришло новое сообщение
