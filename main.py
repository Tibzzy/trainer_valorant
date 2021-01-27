import serial
from noRecoil import NoRecoil
from trigger import Trigger
from win32 import win32api
import threading
import queue
from time import sleep
import os


serialHandle = serial.Serial('COM7', 9600)

#Call Cheat
nR = NoRecoil(serialHandle)
tR = Trigger(serialHandle)

#Var ativado ou desativado
firstOption=True
beforeFirstOption=1
secondOption=True
beforeSecondOption=1

#Variavel para ser adicionada a thread para receber o valor enquanto a thread estiver sendo executada
noRecoil_Queue = queue.Queue()
trigger_Queue = queue.Queue()
noRecoil_Queue_trigger = queue.Queue()

def enableOrNo():
    os.system('cls')
    print("noRecoil ---> Desativado") if beforeFirstOption==1 else print("noRecoil ---> Ativado")
    print("trigger ---> Desativado") if beforeSecondOption==1 else print("trigger ---> Ativado")

enableOrNo()

#MENU
while True:
    #Ativa e Desativa o noRecoil // Press (F1)
    """
        api do windows para identificar quando apertar o botão F1 do teclado
    """
    if win32api.GetKeyState(0x70) == -127 or win32api.GetKeyState(0x70) == -128:
        if firstOption:
            if beforeFirstOption==1:
                """
                    Cria uma thread e inicia ela.
                    Essa thread chama o objeto 'noRecoil' que ativa a função de remover o recoil da arma no Valorant pelo Arduino Leonardo R3
                """
                t1 = threading.Thread(target=nR.noRecoil, args=(noRecoil_Queue,))
                t1.start()
                noRecoil_Queue_trigger.put(True)
                beforeFirstOption=2
                enableOrNo()
                firstOption=False
        else:
            if beforeFirstOption==2:
                """
                    Atualiza a variavel da thread com o valor Falso para encerrar o While no objeto
                """
                noRecoil_Queue.put(False)
                noRecoil_Queue_trigger.put(False)
                beforeFirstOption=1
                enableOrNo()
                firstOption=True
        sleep(1)

    if win32api.GetKeyState(0x71) == -127 or win32api.GetKeyState(0x71) == -128:
        if secondOption:
            if beforeSecondOption==1:
                """
                    Cria uma thread e inicia ela.
                    Essa thread chama o objeto 'trigger' que ativa o trigger bot no Valorant pelo Arduino Leonardo R3
                """
                t2 = threading.Thread(target=tR.trigger, args=(trigger_Queue, noRecoil_Queue_trigger))
                t2.start()
                beforeSecondOption=2
                enableOrNo()
                secondOption=False
        else:
            if beforeSecondOption==2:
                """
                    Atualiza a variavel da thread com o valor Falso para encerrar o While no objeto
                """
                trigger_Queue.put(False)
                beforeSecondOption=1
                enableOrNo()
                secondOption=True
        sleep(1)

    if win32api.GetKeyState(0x72) == -127 or win32api.GetKeyState(0x72) == -128:
        print("Trainer Encerrado!!!")
        noRecoil_Queue.put(False)
        break