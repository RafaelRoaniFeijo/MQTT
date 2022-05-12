# Simulando-dados-de-um-sensor-MQTT
MQTT
Publicar no tópico sisdis/sensores
Os valores devem ser ramdomizados a cada leitura(simulados)
Enviar uma leitura a cada 5 segundos
Contrato: 
Formato json
Enviar um dicionário contendo as chaves
Chave		tipo		descrição
IDSENSOR	      INTEIRO	  ID DO SENSOR
TEMPERATURA	      FLOAT		TEMPERATURA EM GRAUS CELCIUS, INTERVALO [-100... 300]
UMIDADE	            INT		UMIDADE EM PERCENTUAL. Intervalo[0... 100]
Escopo: 
Cada leitura é um valor digitado;
Desserializar a mensagem; 
