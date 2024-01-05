import pygame
import pyxinput
import numpy as num

# Get controller inputs with pygame
pygame.init()

j = pygame.joystick.Joystick(1)
j.init()

# Uncomment all commented code lines to have two controllers
#j2 = pygame.joystick.Joystick(0)
#j2.init()

mycontroller = pyxinput.vController()
#mycontroller2 = pyxinput.vController(1)

# The buttons are indexed by the received button number from pygame
buttons = ["BtnY","BtnB","BtnA","BtnX","BtnShoulderL","BtnShoulderR","TriggerL","TriggerR","BtnBack","BtnStart"]

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

try:
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYBUTTONDOWN or pygame.JOYBUTTONUP:
                for i, x in enumerate(buttons):
                    # First Controller
                    if j.get_button(i):
                        print(x)
                        mycontroller.set_value(x, 1)
                    else:
                        mycontroller.set_value(x, 0)
                    # Second controller
                    #if j2.get_button(i):
                    #    print(x)
                    #    mycontroller2.set_value(x, 1)
                    #else:
                    #    mycontroller2.set_value(x, 0)
                
            if event.type == pygame.JOYAXISMOTION:
                mycontroller.set_value('AxisLx',num.ceil(j.get_axis(0)*100)/100)
                mycontroller.set_value('AxisLy',num.ceil(-j.get_axis(1)*100)/100)
                mycontroller.set_value('AxisRy',num.ceil(-j.get_axis(2)*100)/100)
                mycontroller.set_value('AxisRx',num.ceil(j.get_axis(3)*100)/100)
                
                #mycontroller2.set_value('AxisLx',num.ceil(j2.get_axis(0)*100)/100)
                #mycontroller2.set_value('AxisLy',num.ceil(-j2.get_axis(1)*100)/100)
                #mycontroller2.set_value('AxisRy',num.ceil(-j2.get_axis(2)*100)/100)
                #mycontroller2.set_value('AxisRx',num.ceil(j2.get_axis(3)*100)/100)

            if event.type == pygame.JOYHATMOTION:
                for rl in -1, 1, 0:
                    for ud in -1, 1, 0:
                        if j.get_hat(0)[0] == rl:              
                            if j.get_hat(0)[1] == ud:
                                # Construct dpa dictionary input
                                distr = "0"+str(rl)+"_"+"1"+str(ud)
                                print(distr)
                                mycontroller.set_value("Dpad", dpa[distr])
                        #if j2.get_hat(0)[0] == rl:              
                        #    if j2.get_hat(0)[1] == ud:
                        #        distr = "0"+str(rl)+"_"+"1"+str(ud)
                        #        print(distr)
                        #        mycontroller2.set_value("Dpad", dpa[distr])
       
except KeyboardInterrupt:
    print("EXITING NOW")
    j.quit()
