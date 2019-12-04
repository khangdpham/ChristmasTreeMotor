import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
def SetupPin(p):
  GPIO.setup(p,GPIO.OUT)
  GPIO.output(p,GPIO.HIGH)
def TurnOff(p):
  GPIO.output(p,GPIO.HIGH)
def TurnOn(p):
  GPIO.output(p,GPIO.LOW)

Pins=[2,3,4,17,27,22,10,9]
for p in Pins:
  SetupPin(p)
for p in Pins:
  TurnOn(p)
  time.sleep(.2)
for p in Pins:
  TurnOff(p)
  



