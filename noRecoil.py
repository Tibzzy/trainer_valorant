from win32 import win32api
from time import sleep

class NoRecoil:
    def __init__(self, serialArduino):
        self.serialArd = serialArduino

    def noRecoil(self, flagStop_Queue):
        before_action_ard=1
        flagStop = True
        while flagStop:
            try:
                flagStop = flagStop_Queue.get_nowait()
            except:
                if win32api.GetKeyState(0x01) == -127 or win32api.GetKeyState(0x01) == -128:
                    if before_action_ard != 1:
                        self.serialArd.write(b'11')
                    before_action_ard=1
                elif win32api.GetKeyState(0x01) == 0 or win32api.GetKeyState(0x01) == 1:
                    if before_action_ard != 0:
                        self.serialArd.write(b'00')
                    before_action_ard=0