from pyboy import PyBoy, WindowEvent
import random
import fnmatch
import os
import cv2
import numpy as np
from time import sleep
import time

pyboy = PyBoy('red.gb', sound=True)
buttons = ['up', 'down', 'left', 'right', 'a', 'b', 'start', 'select']

endtime = time.time() + 1

def screenshot():
    pyboy.send_input(WindowEvent.SCREENSHOT_RECORD)
    for file in os.listdir('screenshots'):
        if fnmatch.fnmatch(file, '*'):
            old_file = os.path.join("screenshots", file)
            new_file = os.path.join("screenshots", "screen.png")
            os.rename(old_file, new_file)
            check(new_file)

def check(new_file):
    screen_path = os.path.join(os.getcwd(), 'screenshots', 'screen.png');
    for objects in os.listdir("objects"):
        object_path = os.path.join(os.getcwd(), 'objects', objects)
        img_rgb = cv2.imread(screen_path)
        template = cv2.imread(object_path)
        res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
        threshold = .8
        if np.amax(res) > threshold:
            checked = os.path.splitext(objects)[0]
            if checked == 'title':
                print('title')
                pyboy.send_input(WindowEvent.PRESS_BUTTON_START)
                pyboy.tick()
                pyboy.tick()
                pyboy.send_input(WindowEvent.RELEASE_BUTTON_START) 
            elif checked == 'new':
                print('new')
                pyboy.send_input(WindowEvent.PRESS_BUTTON_A)
                pyboy.tick()
                pyboy.tick()
                pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)    
    os.remove(new_file)      
    move()

def move():
    rand = random.choice(buttons)
    if rand == 'up':
        print(rand)
        pyboy.send_input(WindowEvent.PRESS_ARROW_UP)
        pyboy.tick()
        pyboy.tick()
        pyboy.send_input(WindowEvent.RELEASE_ARROW_UP)      
    elif rand == 'down':
        print(rand)
        pyboy.send_input(WindowEvent.PRESS_ARROW_DOWN)
        pyboy.tick()
        pyboy.tick()
        pyboy.send_input(WindowEvent.RELEASE_ARROW_DOWN)      
    if rand == 'right':
        print(rand)       
        pyboy.send_input(WindowEvent.PRESS_ARROW_RIGHT)
        pyboy.tick()
        pyboy.tick()
        pyboy.send_input(WindowEvent.RELEASE_ARROW_RIGHT)
    elif rand == 'left':
        print(rand)
        pyboy.send_input(WindowEvent.PRESS_ARROW_LEFT)
        pyboy.tick()
        pyboy.tick()
        pyboy.send_input(WindowEvent.RELEASE_ARROW_LEFT)
    elif rand == 'a':
        print(rand)
        pyboy.send_input(WindowEvent.PRESS_BUTTON_A)
        pyboy.tick()
        pyboy.tick()
        pyboy.send_input(WindowEvent.RELEASE_BUTTON_A)        
    elif rand == 'b':
        print(rand)
        pyboy.send_input(WindowEvent.PRESS_BUTTON_B)
        pyboy.tick()
        pyboy.tick()
        pyboy.send_input(WindowEvent.RELEASE_BUTTON_B)      
    elif rand == 'start':
        print(rand)
        pyboy.send_input(WindowEvent.PRESS_BUTTON_START)
        pyboy.tick()
        pyboy.tick()
        pyboy.send_input(WindowEvent.RELEASE_BUTTON_START)       
    elif rand == 'select':
        print(rand)
        pyboy.send_input(WindowEvent.PRESS_BUTTON_SELECT)
        pyboy.tick()
        pyboy.tick()
        pyboy.send_input(WindowEvent.RELEASE_BUTTON_SELECT)
        
while not pyboy.tick():
    if time.time() < endtime:
        pass
    else:
        endtime = time.time() + 1
        screenshot()
