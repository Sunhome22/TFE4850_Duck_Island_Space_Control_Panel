from gpiozero import MCP3008
from gpiozero import LED
from gpiozero import Button
from time import sleep
from signal import pause
import socket
import os
import math
from dotenv import load_dotenv, dotenv_values, find_dotenv

load_dotenv(find_dotenv(".dev.env"))

# Constans
HOST = os.environ.get("HOST")
PORT = int(os.environ.get("PORT"))
ALPHA = 0.05 #EMA

# Global values
ema_value = 0

# Pin assignments
button0Pin = Button(17, bounce_time = 0.1)
button1Pin = Button(27, bounce_time = 0.1)
button2Pin = Button(22, bounce_time = 0.1)
button3Pin = Button(5, bounce_time = 0.1)
button4Pin = Button(6, bounce_time = 0.1)
button5Pin = Button(26, bounce_time = 0.1)
led1Pin = LED(23)
led2Pin = LED(24)
led3Pin = LED(25)
led4Pin = LED(12)
led5Pin = LED(16)
potPin = MCP3008(0)

# Turns on all LEDs initially
led1Pin.on()
led2Pin.on()
led3Pin.on()
led4Pin.on()
led5Pin.on()

# Sets initial previous button states
prevButton0PinValue = 1
prevButton1PinValue = 1
prevButton2PinValue = 1
prevButton3PinValue = 1
prevButton4PinValue = 1
prevButton5PinValue = 1

buttons = [
    {"pin": button0Pin, "prevValue": prevButton0PinValue, "onCommand": b"B0-ON [/TCP]"},
    {"pin": button1Pin, "prevValue": prevButton1PinValue, "onCommand": b"B1-ON [/TCP]"},
    {"pin": button2Pin, "prevValue": prevButton2PinValue, "onCommand": b"B2-ON [/TCP]"},
    {"pin": button3Pin, "prevValue": prevButton3PinValue, "onCommand": b"B3-ON [/TCP]"},
    {"pin": button4Pin, "prevValue": prevButton4PinValue, "onCommand": b"B4-ON [/TCP]"},
    {"pin": button5Pin, "prevValue": prevButton5PinValue, "onCommand": b"B5-ON [/TCP]"},
]

# Binds actions to button input
button1Pin.when_pressed = led1Pin.off
button2Pin.when_pressed = led2Pin.off
button3Pin.when_pressed = led3Pin.off
button4Pin.when_pressed = led4Pin.off
button5Pin.when_pressed = led5Pin.off
button1Pin.when_released = led1Pin.on
button2Pin.when_released = led2Pin.on
button3Pin.when_released = led3Pin.on
button4Pin.when_released = led4Pin.on
button5Pin.when_released = led5Pin.on

# Sends button presses and potentiometer value with websockets when change is detected
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    while True:
        for button in buttons:
            if button["pin"].is_pressed and button["prevValue"] == 0:
                button["prevValue"] = 1
                s.sendall(button["onCommand"])
                data = s.recv(1)
            elif not button["pin"].is_pressed:
                button["prevValue"] = 0

        prevPotValue = round(ema_value)

        # EMA filter
        ema_value = ALPHA * round(potPin.value*200-100, 1) + (1-ALPHA) * ema_value
        print(ema_value)

        if prevPotValue != round(ema_value):
           s.send((str(round(ema_value)) + "[/TCP]").encode("utf-8"))
           data = s.recv(128)

# Keep listening for button presses
pause()



