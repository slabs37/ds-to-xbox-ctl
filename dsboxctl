import pygame
import pyxinput
import numpy as num

# Get controller inputs with pygame
pygame.init()

j = pygame.joystick.Joystick(1)
j.init()

# Uncomment these to have two controllers
#j2 = pygame.joystick.Joystick(0)
#j2.init()

mycontroller = pyxinput.vController()
#mycontroller2 = pyxinput.vController(1)

# The buttons are indexed by the received button number from pygame
buttons = ["BtnY","BtnB","BtnA","BtnX","BtnShoulderL","BtnShoulderR","TriggerL","TriggerR","BtnBack","BtnStart"]

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
       
except KeyboardInterrupt:
    print("EXITING NOW")
    j.quit()
