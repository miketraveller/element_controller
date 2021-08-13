#!/usr/bin/env python3

import time
import threading
import digitalio
import board

ssr = digitalio.DigitalInOut(board.D26)
ssr.direction = digitalio.Direction.OUTPUT

flag = 1
spacing = 1.0

def cycle():
  global flag
  global spacing
  global ssr

  while flag == 1:
#    print("hi")
    ssr.value = True
    time.sleep(spacing * 2)

#    print("low")
    ssr.value = False
    time.sleep(2 - (spacing * 2))

    if flag == False:
      print("end loop")

def get_input():
  global flag
  global spacing
  global ssr

  while flag == 1:

    key = input("Enter new ratio or q to quit: ")

    if key == 'q':
      print("terminating gracefully")
      ssr.value = False
      flag = False
    else:
      spacing = float(key) 
      print("updated duty cycle to ", key)

duty_cycle = threading.Thread(target=cycle)
inputs = threading.Thread(target=get_input)

duty_cycle.start()
inputs.start()
