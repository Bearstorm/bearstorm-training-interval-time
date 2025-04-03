import paho.mqtt.client as mqtt_lib
import json

mqtt = mqtt_lib.Client()
status_data = {}

def init_app(app):
    mqtt.connect("localhost", 1883, 60)
    mqtt.loop_start()
    mqtt.subscribe("bearstorm/timer/status")
    mqtt.on_message = on_message

def send_command(command):
    mqtt.publish("bearstorm/timer/command", command)

def send_settings(data):
    mqtt.publish("bearstorm/timer/settings", json.dumps(data))

def on_message(client, userdata, msg):
    global status_data
    if msg.topic == "bearstorm/timer/status":
        status_data = json.loads(msg.payload.decode())

def get_status():
    return status_data or {
        "mode": "IDLE",
        "round": 0,
        "time_left": 0
    }
