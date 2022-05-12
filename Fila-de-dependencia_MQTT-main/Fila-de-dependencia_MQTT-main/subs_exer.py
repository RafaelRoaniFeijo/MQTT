#CHAMASSE FILA DE DEPENDÊNCIA, escuto o tópico 2 (que o nodo 1 vai enviar), recebo a mensagem e posto no 3 (valor 123)

import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe #receber o valor do broker
import time
def Recebe_do_nodo1 (cliente, userdata, message):
    
    s = message.payload.decode("utf8") 
    r = s +"2"
    publish.single("sisdis/nodo3",r,hostname="mqtt.eclipseprojects.io")   

subscribe.callback(Recebe_do_nodo1, 
                            "sisdis/nodo2", 
                            hostname="mqtt.eclipseprojects.io")