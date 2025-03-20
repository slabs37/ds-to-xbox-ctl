import pygame
import pyxinput
from time import sleep

# Get controller inputs with pygame
pygame.init()

pycontroller = {}
pyxcontroller = {}
# Change this depending on how many controllers you have connected
controllerCount = 2
for i in range(controllerCount):
    pycontroller[i] = pygame.joystick.Joystick(i)
    pycontroller[i].init()
    # pyxinput seems to need the first controller to be empty vController(), doesn't accept 0
    if i == 0:
        pyxcontroller[i] = pyxinput.vController()
    else:
        pyxcontroller[i] = pyxinput.vController(i)



# The buttons are indexed by the received button number from pygame
buttons = ["BtnY","BtnB","BtnA","BtnX","BtnShoulderL","BtnShoulderR","TriggerL","TriggerR","BtnBack","BtnStart","BtnThumbL","BtnThumbR"]

# dpad buttons, from pygame's input to pyxinput's values
dpa = {
    "01_10" : 8,
    "0-1_10" : 4,
    "00_11" : 1,
    "00_1-1" : 2,
    "0-1_11" : 5,
    "0-1_1-1" : 6,
    "01_11" : 9,
    "01_1-1" : 10,
    "00_10" : 0,
}    

def doJoysticks(event, controller):
    if event.type == pygame.JOYAXISMOTION:
        pyxcontroller[controller].set_value('AxisLx',round(int(pycontroller[controller].get_axis(0)*100.01)/100, 2))
        pyxcontroller[controller].set_value('AxisLy',round(int(-pycontroller[controller].get_axis(1)*100.01)/100, 2))
        pyxcontroller[controller].set_value('AxisRy',round(int(-pycontroller[controller].get_axis(2)*100.01)/100, 2))
        pyxcontroller[controller].set_value('AxisRx',round(int(pycontroller[controller].get_axis(3)*100.01)/100, 2))

def doButtons(event, controller):
    if event.type == pygame.JOYBUTTONDOWN or pygame.JOYBUTTONUP:
        for i, x in enumerate(buttons):
            if pycontroller[controller].get_button(i):
                pyxcontroller[controller].set_value(x, 1)
            else:
                pyxcontroller[controller].set_value(x, 0)

def doDpad(event, controller):
    if event.type == pygame.JOYHATMOTION:
        for rl in -1, 1, 0:
            for ud in -1, 1, 0:
                if pycontroller[controller].get_hat(0)[0] == rl:                  
                    if pycontroller[controller].get_hat(0)[1] == ud:
                        # Construct dpa dictionary input
                        distr = "0"+str(rl)+"_"+"1"+str(ud)
                        pyxcontroller[controller].set_value("Dpad", dpa[distr])

def printControllers():
    text = ""
    for n in range(controllerCount):
        text = text + f"Controller {n+1}, Left Joystick Pos : {pycontroller[n].get_axis(0):.2f} {-pycontroller[n].get_axis(1)+0.001:.2f}    "
    print("\r" + text, end="")

def __main__():
    try:
        print(f"Connected {controllerCount} controllers")
        while True:
            events = pygame.event.get()
            for event in events:
                for n in range(controllerCount):
                    doButtons(event, n)
                    doJoysticks(event, n)
                    doDpad(event, n)
            printControllers()
            # For decreasing cpu usage :)
            sleep(0.001)
           
            
    except KeyboardInterrupt:
        print("EXITING NOW")
        for i in range(controllerCount):
            pycontroller[i].quit()

__main__()
