#!/usr/bin/env python

import dothat.backlight as backlight
import dothat.lcd as lcd
#import signal
import atexit
import time

rain = [
    [1,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0],
    [0,0,2,0,0,0,0,0],
    [0,0,0,2,0,0,0,0],
    [0,0,0,0,4,0,0,0],
    [0,0,0,0,0,4,0,0],
    [0,0,0,0,0,0,8,0],
    [0,0,0,0,0,0,0,16],
    [0,0,0,0,0,0,0,0]
]

def tidyup():
    backlight.off()
    lcd.clear()

def get_anim_frame(char,fps):
    return char[ int(round(time.time()*fps) % len(char)) ]

backlight.graph_off()
backlight.off()

lcd.set_cursor_position(0,0)
lcd.write(chr(0) * 16)
lcd.set_cursor_position(0,1)
lcd.write(chr(0) * 16)
lcd.set_cursor_position(0,2)
lcd.write(chr(0) * 16)

time.sleep(1)
for x in range(0,255,5):
    backlight.single_rgb(3,x,x,x)

atexit.register(tidyup)

while True:
    lcd.create_char(0,get_anim_frame(rain,20))
    time.sleep(0.1)
#signal.pause()
