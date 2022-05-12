import paho.mqtt.publish as publish
import json
import random
import time
idsensor=2
while True:
    d = {}
    d["IDSENSOR"] = 2
    d["TEMPERATURA"] = random.randrange(-100,300)
    d["UMIDADE"] = random.randint(0,100)
    publish.single("sisdis/sensores",json.dumps(d),hostname="mqtt.eclipseprojects.io")
    time.sleep(5)


