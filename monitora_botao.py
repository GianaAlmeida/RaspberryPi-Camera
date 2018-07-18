#Bibliotecas utilizadas
import RPi.GPIO as GPIO
import os
import time


gpio_monitorado = 4                   # GPIO4, pino 7
GPIO.setmode(GPIO.BCM)                # Estou dizendo que vou informar um GPIO ao inves do pino (modularizacao)
GPIO.setup(gpio_monitorado, GPIO.IN)  # define o pino7 / GPIO4 como entrada

def chama_camera():
    while 1:
        if (GPIO.input(gpio_monitorado) == False):
            # Sistema Operacional executa como root
             os.system("sudo python /home/pi/script/liga_camera.py")
            # os.system("sh /home/pi/script/bate_foto")
            
chama_camera()
