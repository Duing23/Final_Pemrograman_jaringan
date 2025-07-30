import paho.mqtt.client as mqtt
import json
import time
import random

client = mqtt.Client()

# 🔐 Tambahkan username & password
client.username_pw_set("ekandanguser", "Ekandangpass")

# 🔁 Sambungkan ke broker di port 1885
client.connect("localhost", 1885, 60)

print("Publisher e-Kandang aktif...")

while True:
    suhu = round(random.uniform(28.0, 38.0), 2)
    data = {"suhu": suhu}
    client.publish("ekandang/suhu", json.dumps(data))
    print("Dikirim:", data)
    time.sleep(5)
