import vk
import time
session = vk.Session('e97cb4a1bd10aba5a8fb574cda2a609b4bb1d2c3448cdd566e0533f9936571ac1c4613370d2bbaf44c3ec')
api = vk.API(session)
while True:
    if (time.time() // 1) == 1527793200.0:
        api.board.createComment(group_id='7812524', topic_id='38431921', message="ШР - СССР на 20.10, согласовано", v='5.78')
        time.sleep(2)

