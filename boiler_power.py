#!/usr/bin/env python3

import time
import threading
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(26, gpio.OUT)

flag = 1
spacing = 1.0

def cycle():
  global flag
  global spacing
  global ssr

  while flag == 1:
#    print("hi")
    gpio.output(26, gpio.HIGH)
    time.sleep(spacing * 2)

#    print("low")
    gpio.output(26, gpio.LOW)
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
      gpio.output(26, gpio.LOW)
      flag = False
    else:
      spacing = float(key) 
      print("updated duty cycle to ", key)

duty_cycle = threading.Thread(target=cycle)
inputs = threading.Thread(target=get_input)

duty_cycle.start()
inputs.start()
