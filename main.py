import vk_api
import requests
import datetime
import random
from vk_api.longpoll import VkLongPoll, VkEventType
now = datetime.datetime.now()
session = requests.Session()

token='d43183177e20c8307a7815180aaef13a8b56a0b7e63b06697001cae96f98248680a5dbf2e04969b047aac'
days_counter = [0,0,0,0]

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id":random.randint(1,1000)})

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

# Основной цикл
for event in longpoll.listen():

    d =datetime.datetime.now().hour
    if datetime.datetime.today().weekday() == 1 and (18> d >=14):
        if days_counter[0] !=1:
            write_msg(event.user_id, "завтра ОБЖ! всем принести тетрадки, иначе не будем смотреть видео, а будем писать в тетрадках!")
            days_counter[0] = 1
    if datetime.datetime.today().weekday() == 1 and (20>d >=18):
        if days_counter[1] != 1:
            write_msg(event.user_id, "завтра ОБЖ! всем принести тетрадки, иначе не будем смотреть видео, а будем писать в тетрадках!")
            days_counter[1] = 1
    if datetime.datetime.today().weekday() == 1 and (23>d >=20):
        if days_counter[2] != 1:
            write_msg(event.user_id, "завтра ОБЖ! всем принести тетрадки, иначе не будем смотреть видео, а будем писать в тетрадках!")
            days_counter[2] = 1
    if datetime.datetime.today().weekday() == 2 and (d >=9):
        if days_counter[3] != 1:
            write_msg(event.user_id, "сегодя ОБЖ! всем принести тетрадки, иначе не будем смотреть видео, а будем писать в тетрадках!")
            days_counter[3] = 1
    if datetime.datetime.today().weekday() == 2 and (d >9):
        days_counter = [0,0,0,0]
    # Если пришло новое сообщение

