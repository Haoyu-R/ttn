import time
import ttn
import re
app_id = "smart_traffic"
access_key = "ttn-account-v2.8vH1qb_0uZ26X73RLiwh8rqC-oVlylURlj5r6kyFqvg"

def uplink_callback(msg, client):
  print("Received uplink from ", msg.dev_id)
  msg_str = str(msg)
  msg_lit = re.split(r'[\s\,\=\(\)]', msg_str)
  print('Current counter: {}'.format(msg_lit[14]))
  print('Current wifi: {}'.format(msg_lit[23]))


try:
    handler = ttn.HandlerClient(app_id, access_key)

    # using mqtt client
    mqtt_client = handler.data()
    mqtt_client.set_uplink_callback(uplink_callback)
    mqtt_client.connect()
    time.sleep(61)
    mqtt_client.close()

    # # using application manager client
    app_client =  handler.application()
    my_app = app_client.get()
    # print(my_app)
    my_devices = app_client.devices()
    # print(my_devices)
except RuntimeError:
    print('pass')