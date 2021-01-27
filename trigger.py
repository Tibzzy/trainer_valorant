import pyautogui
from time import sleep

class Trigger:
    def __init__(self, serialArduino):
        self.serialArd = serialArduino
        self.pixel_list = []

    def trigger(self, flagStop_Queue, flag_Recoil_Queue):
        flagStop=True
        flag_Recoil=False
        while flagStop:
            try:
                flagStop = flagStop_Queue.get_nowait()
            except:
                try:
                    flag_Recoil = flag_Recoil_Queue.get_nowait()
                except:
                    img = pyautogui.screenshot(region=(955, 535, 10, 10))
                    self.pixel_list.clear()

                    for x in range(10):
                        for y in range(10):
                            self.pixel_list.append(img.getpixel((x,y)))

                    for pixel in self.pixel_list:
                        if pixel[0] >= 120 and pixel[1] <= 110 and pixel[2] >= 140 :
                            if flag_Recoil:
                                self.serialArd.write(b'21')
                            else:
                                self.serialArd.write(b'20')
                            self.serialArd.write(b'00')
                            break
                    sleep(0.1)