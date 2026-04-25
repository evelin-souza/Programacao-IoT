#Author: Evelin de Souza Batista Silva
import time
from machine import Pin


#Semaforo 1
led_verm_1 = Pin(26, Pin.OUT)
led_amr_1 = Pin(27, Pin.OUT)
led_vrd_1 = Pin(14, Pin.OUT)

#Semaforo 2
led_verm_2 = Pin(17, Pin.OUT) #antes "= Pin(5, Pin.OUT)" fazia com que o LED iniciasse antes do botao de início ser pressionado
led_amr_2 = Pin(16, Pin.OUT)
led_vrd_2 = Pin(4, Pin.OUT)

#botoes
btn_start_verde = Pin(0, Pin.IN, Pin.PULL_UP)
btn_stop_vermelho = Pin(2, Pin.IN, Pin.PULL_UP)


#desligar
def desligar():
  led_verm_1.value(0)
  led_amr_1.value(0)
  led_vrd_1.value(0)
  led_verm_2.value(0)
  led_amr_2.value(0)
  led_vrd_2.value(0)
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
        #   1) Inicialmente, o semáforo 1 está no verde e o semáforo 2 no vermelho.

        #semaforo1
        led_verm_1.value(0)
        led_amr_1.value(0)
        led_vrd_1.value(1)

        #semaforo2
        led_verm_2.value(1)
        led_amr_2.value(0)
        led_vrd_2.value(0)
        time.sleep(10) 
        if btn_stop_vermelho.value() == 0: rodando = False; continue

        #   2) Depois de um tempo especificado, o semáforo 1 apaga a luz verde e aciona a luz amarela.
        #semaforo1
        led_verm_1.value(0)
        led_amr_1.value(1)
        led_vrd_1.value(0)

        #semaforo2
        led_verm_2.value(1)
        led_amr_2.value(0)
        led_vrd_2.value(0)
        time.sleep(2)
        if btn_stop_vermelho.value() == 0: rodando = False; continue

        # Novamente, passado um tempo especificado, o semáforo 1 aciona o vermelho e apaga o amarelo, enquanto o semáforo 2 apaga o vermelho e aciona o verde.
        led_verm_1.value(1)
        led_amr_1.value(0)
        led_vrd_1.value(0)

        #semaforo2
        led_verm_2.value(0)
        led_amr_2.value(0)
        led_vrd_2.value(1)
        time.sleep(10)
        if btn_stop_vermelho.value() == 0: rodando = False; continue
            
        # Novamente, passado um tempo especificado, o semáforo 1 aciona o vermelho e apaga o amarelo, enquanto o semáforo 2 apaga o vermelho e aciona o verde.
        #semaforo1
        led_verm_1.value(1)
        led_amr_1.value(0)
        led_vrd_1.value(0)
        #semaforo2
        led_verm_2.value(0)
        led_amr_2.value(1)
        led_vrd_2.value(0)
        time.sleep(2)

        # O ciclo se repete até que o botão desligar seja pressionado.

#_____________________________________________________________________________________________________________________
#|     NOTA: Devido ao uso da funcao time.sleep(), o sistema fica "ocupado" durante a contagem.                       |
#|     Para garantir que o botao VERMELHO (botao desligar) funcione, mantenha-o pressionado até que o semaforo mude.  |
#|     O desligamento ocorrerá assim que o tempo do LED atual erminar e o código ler a entrada novamente.             |
#|____________________________________________________________________________________________________________________|


#_________________________________________________________________________________________
#|                              ESPECIFICACOES DA ATIVIDADE:                              |
#|          LED AMARELO DEVE FICAR LIGADO POR 2 SEGUNDOS.                                 |
#|          LED VERDE DEVE FICAR LIGADO POR 10 SEGUNDOS.                                  |
#|          CADA LUZ É CONTROLADA USANDO UMA PORTA DA PLACA.                              |
#|          UTILIZAR LEDS E RESISTORES PARA SIMULAR LUZES VERDE, AMARELA E VERMELHA.      |
#|          UTILIZAR BOTAO PARA INICIAR CICLO DOS SEMAFOROS                               |
#|          UTILIZAR SEGUNDO BOTAR PARA FINALIZAR CICLO DOS SEMAFOROS.                    |
#|________________________________________________________________________________________|
