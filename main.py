import json

import vk
import requests
import datetime
from flask import Flask

app = Flask(__name__)
now = datetime.datetime.now()


token='d43183177e20c8307a7815180aaef13a8b56a0b7e63b06697001cae96f98248680a5dbf2e04969b047aac'
group_id = 212652278

@app.route("/", methods=['POST'])
def processing():
    data = json.loads(requests.data)
    session = requests.Session()
    api = vk.API(session)
    api.messages.send(access_token=token, chat_id=group_id,message="asdiuhsdfhiusdaihu", random_id=0)

    return ""



# Основной цикл
# for event in longpoll.listen():
#     if not event.from_chat:
#         d =datetime.datetime.now().hour
#         if datetime.datetime.today().weekday() == 2 and (d ==14 or d == 18 or d ==20):
#             write_msg(event.user_id, "завтра ОБЖ! всем принести тетрадки, иначе не будем смотреть видео, а будем писать в тетрадках!")
#         # Если пришло новое сообщение


