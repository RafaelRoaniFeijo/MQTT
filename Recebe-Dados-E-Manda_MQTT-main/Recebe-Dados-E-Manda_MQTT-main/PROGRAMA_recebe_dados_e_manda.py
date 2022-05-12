#Computaçao distribuída sem dependencia, todo mundo recebe tudo e processa tudo. Ex: bate papo
import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe #receber o valor do broker
import json
import random
def Recebe_sinais (cliente, userdata, message):
    d = {}
    d["IDSENSOR"] = 2
    d["TEMPERATURA"] = round(random.uniform(-100, 300), 2) #float
    d["UMIDADE"] = random.randint(0,100) #int
    publish.single("sisdis/sensores",json.dumps(d),hostname="mqtt.eclipseprojects.io")   
                                    #desseraliza e junta todos os d's
subscribe.callback(Recebe_sinais, 
                    "sisdis/sensor2", 
                    hostname="mqtt.eclipseprojects.io")
    