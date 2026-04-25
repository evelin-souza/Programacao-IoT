#Author: Evelin de Souza Batista Silva
import time
from machine import Pin

#buzzer
buzzer = Pin(32, Pin.OUT)

#Semaforo 1
led_verm_1 = Pin(33, Pin.OUT)
led_amr_1 = Pin(25, Pin.OUT)
led_vrd_1 = Pin(26, Pin.OUT)

#Semaforo 2
led_verm_2 = Pin(27, Pin.OUT)
led_amr_2 = Pin(14, Pin.OUT)
led_vrd_2 = Pin(12, Pin.OUT)

#Semaforo 3
led_verm_3 = Pin(23, Pin.OUT)
led_amr_3 = Pin(22, Pin.OUT)
led_vrd_3 = Pin(18, Pin.OUT)

#Semaforo 4
led_verm_4 = Pin(17, Pin.OUT)
led_amr_4 = Pin(16, Pin.OUT)
led_vrd_4 = Pin(4, Pin.OUT)


#botoes
btn_start_verde = Pin(13, Pin.IN, Pin.PULL_UP)
btn_stop_vermelho = Pin(15, Pin.IN, Pin.PULL_UP)


#desligar
def desligar():
  led_verm_1.value(0)
  led_amr_1.value(0)
  led_vrd_1.value(0)
  led_verm_2.value(0)
  led_amr_2.value(0)
  led_vrd_2.value(0)
  led_verm_3.value(0)
  led_amr_3.value(0)
  led_vrd_3.value(0)
  led_verm_4.value(0)
  led_amr_4.value(0)
  led_vrd_4.value(0)
  # Faz o buzzer apitar por meio segundo ao desligar
  buzzer.value(1)
  time.sleep(1.5)
  buzzer.value(0)
rodando = False

print("Aperte o botão verde para iniciar o simulador de semaforo")

while True:

    if btn_start_verde.value() == 0:
        rodando = True
        print("Iniciando semaforo")

    if btn_stop_vermelho.value() == 0:
        rodando = False
        print("Desligando semaforo")
        desligar()
        time.sleep(0.5) #Para evitar mais de uma leitura
    
    if rodando:
        desligar()
        #   1) Inicialmente, o semáforo 1 está no verde e os semáforos 2, 3 e 4 estão no vermelho.

        #semaforo1
        led_verm_1.value(0)
        led_amr_1.value(0)
        led_vrd_1.value(1)

        #semaforo2
        led_verm_2.value(1)
        led_amr_2.value(0)
        led_vrd_2.value(0)

        #semaforo3
        led_verm_3.value(1)
        led_amr_3.value(0)
        led_vrd_3.value(0)

        #semaforo4
        led_verm_4.value(1)
        led_amr_4.value(0)
        led_vrd_4.value(0)

        time.sleep(13) 

        if btn_stop_vermelho.value() == 0: rodando = False; continue

        # O semaforo 1 entra mo amarelo e os semaforos 2, 3 e 4 seguem no vermelho 

        #semaforo1
        led_verm_1.value(0)
        led_amr_1.value(1)
        led_vrd_1.value(0)

        #semaforo2
        led_verm_2.value(1)
        led_amr_2.value(0)
        led_vrd_2.value(0)

        #semaforo 3
        led_verm_3.value(1)
        led_amr_3.value(0)
        led_vrd_3.value(0)

        #semaforo 4
        led_verm_4.value(1)
        led_amr_4.value(0)
        led_vrd_4.value(0)

        time.sleep(5)

        if btn_stop_vermelho.value() == 0: rodando = False; continue

        # O semaforo 1 entra no vermelho, o semaforos 2 e 4 entram no verde e o semaforo 3 permanece no vermelho
        led_verm_1.value(1)
        led_amr_1.value(0)
        led_vrd_1.value(0)

        #semaforo2
        led_verm_2.value(0)
        led_amr_2.value(0)
        led_vrd_2.value(1)

        #semaforo 3
        led_verm_3.value(1)
        led_amr_3.value(0)
        led_vrd_3.value(0)

        #semaforo 4
        led_verm_4.value(0)
        led_amr_4.value(0)
        led_vrd_4.value(1)

        time.sleep(13)

        if btn_stop_vermelho.value() == 0: rodando = False; continue
            
        #Os semaforo 1 e 3 permanecem no vermelho, os semaforos 2 e 4 entram no amarelo
        led_verm_1.value(1)
        led_amr_1.value(0)
        led_vrd_1.value(0)

        #semaforo2
        led_verm_2.value(0)
        led_amr_2.value(1)
        led_vrd_2.value(0)

        #semaforo 3
        led_verm_3.value(1)
        led_amr_3.value(0)
        led_vrd_3.value(0)

        #semaforo 4
        led_verm_4.value(0)
        led_amr_4.value(1)
        led_vrd_4.value(0)

        time.sleep(5)

        if btn_stop_vermelho.value() == 0: rodando = False; continue

        #O semaforo 1 permanece no vermelho, os semaforos 2 e 4 entram em vermelho e o semaforo 3 entra em verde

        #semaforo1
        led_verm_1.value(1)
        led_amr_1.value(0)
        led_vrd_1.value(0)

        #semaforo2
        led_verm_2.value(1)
        led_amr_2.value(0)
        led_vrd_2.value(0)

        #semaforo 3
        led_verm_3.value(0)
        led_amr_3.value(0)
        led_vrd_3.value(1)

        #semaforo 4
        led_verm_4.value(1)
        led_amr_4.value(0)
        led_vrd_4.value(0)

        time.sleep(13)

        if btn_stop_vermelho.value() == 0: rodando = False; continue

        #Os semaforo 1, 2 e 4 permanecem no vermelho, o semaforo 3 entra no amarelo
        led_verm_1.value(1)
        led_amr_1.value(0)
        led_vrd_1.value(0)

        #semaforo2
        led_verm_2.value(1)
        led_amr_2.value(0)
        led_vrd_2.value(0)

        #semaforo 3
        led_verm_3.value(0)
        led_amr_3.value(1)
        led_vrd_3.value(0)

        #semaforo 4
        led_verm_4.value(1)
        led_amr_4.value(0)
        led_vrd_4.value(0)

        time.sleep(5)  
        if btn_stop_vermelho.value() == 0: rodando = False; continue

        # O ciclo se repete até que o botão desligar seja pressionado.

#_____________________________________________________________________________________________________________________
#|     NOTA: Devido ao uso da funcao time.sleep(), o sistema fica "ocupado" durante a contagem.                       |
#|     Para garantir que o botao VERMELHO (botao desligar) funcione, mantenha-o pressionado até que o semaforo mude.  |
#|     O desligamento ocorrerá assim que o tempo do LED atual erminar e o código ler a entrada novamente.             |
#|____________________________________________________________________________________________________________________|

