#coding=utf-8
from flask import Flask, render_template
from gpiozero import RGBLED
from time import sleep

app = Flask(__name__)

led = RGBLED(red=10, green=9, blue=11)
led.color = (1, 1, 1)


@app.route('/')
def dashboard(error=""):
    user = u"Ariel Jiménez"
    return render_template('base.j2', user = user, error=error)


@app.route("/led/<color>/<state>")
def set_led(color, state):
    if color == "red":
        if state == "on":
            redOn()
        else:
            redOff()
    elif color == "green":
        if state == "on":
            greenOn()
        else:
            greenOff()
    elif color == "blue":
        if state == "on":
            blueOn()
        else:
            blueOff()
    else:
        dashboard("Error en solicitud.")


def color(R, G, B):
  led.color = (R, G, B)

def turnOff():
  print("Apagando las luces:")
  x = 0.0

  while x <= 1:
	led.color = (x, x, x)
    	x += 0.1


def redOn():
  led.red = 0


def greenOn():
  led.green = 0


def blueOn():
  led.blue = 0


def yellowOn():
  color(0, 0, 1)


def cyanOn():
  color(1, 0, 0)


def magentaOn():
  color(0, 1, 0)


def whiteOn():
  color(0, 0, 0)


def redOff():
  led.red = 1


def greenOff():
  led.green = 1


def blueOff():
  led.blue = 1


def yellowOff():
  led.red = 1
  led.green = 1


def cyanOff():
  led.green = 1
  led.blue = 1


def magentaOff():
  led.red = 1
  led.blue = 1


def whiteOff():
  led.red = 1
  led.green = 1
  led.blue = 1
