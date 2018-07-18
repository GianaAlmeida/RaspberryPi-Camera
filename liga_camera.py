####    Codigo em python-picamera    ####

#!/usr/bin/python
import time 
import datetime
from picamera import * 

def nomear_foto() :
    data = datetime.datetime.now()                            # Pegando os dados de tempo nesse exato momento.
    nome = ( 'Bruna' + str(data.year) +                       # Aqui foi feito uma soma de strings, como dia, mes, ano,
           str(data.month) + str(data.day) +                  #    hora, minuto, segundo e microsegundos sao numeros, usamos 
           str(data.hour) + str(data.minute) +                #    ~str~ para converter de numero para texto (string).
           str(data.second) + str(data.microsecond) + '.jpg')
    return nome                                               # Retorna o nome criado 
    
def tira_foto() :
    camera = PiCamera()            #Criando objeto camera com atributos e metodos para raspberry.
    segundos = 2                   #Definindo tempo de abertura antes de finalizar foto.

    nome_foto = nomear_foto()      #O nome eh criado pela funcao anterior, assim garantimos fotos sem nomes repetidos.

    camera.resolution = (800, 600) #Definindo o tamanho da foto em 800x600.
    time.sleep(segundos)           #Executando tempo de abertura.
    camera.capture(nome_foto)      #Captura foto e salva com o nome salvo anteriormente.
    camera.close()                 #Desliga a camera.
    return


tira_foto()                        #Executa a funcao tira_foto ao chamar esse script