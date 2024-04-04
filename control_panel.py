from gpiozero import MCP3008
from gpiozero import LED
from gpiozero import Button
from time import sleep
from signal import pause
import keyboard

# Pin assignments
button0Pin = Button(17)
button1Pin = Button(27)
button2Pin = Button(22)
button3Pin = Button(5)
button4Pin = Button(6)
button5Pin = Button(26)

led1Pin = LED(23)
led2Pin = LED(24)
led3Pin = LED(25)
led4Pin = LED(12)
led5Pin = LED(16)
pot = MCP3008(0)

# Turn on all LEDs initially
led1Pin.on()
led2Pin.on()
led3Pin.on()
led4Pin.on()
led5Pin.on()

def button0():
    print("button 1")

def button1():
    led1Pin.off()

def button2():
    led2Pin.off()

def button3():
    led3Pin.off()

def button4():
    led4Pin.off()
    
def button5():
    led5Pin.off()

# Binds actions to button input
button0Pin.when_pressed = button0
button1Pin.when_pressed = button1
button2Pin.when_pressed = button2
button3Pin.when_pressed = button3
button4Pin.when_pressed = button4
button5Pin.when_pressed = button5
button1Pin.when_released = led1Pin.on
button2Pin.when_released = led2Pin.on
button3Pin.when_released = led3Pin.on
button4Pin.when_released = led4Pin.on
button5Pin.when_released = led5Pin.on

# Keep listening for button presse
pause()
