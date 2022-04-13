import vk_api
import requests
import datetime
from vk_api.longpoll import VkLongPoll, VkEventType
now = datetime.datetime.now()
session = requests.Session()
vk_session = vk_api.VkApi(token='d43183177e20c8307a7815180aaef13a8b56a0b7e63b06697001cae96f98248680a5dbf2e04969b047aac')

event=VkEventType(vk_session)

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
def main():
    try:
        vk_session.auth(token_only=True)
        vk.messages.send(
            user_id=event.user_id,
            message= str(now.strftime("%H:%M"))
        )
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

if __name__ == '__main__':
    main()


