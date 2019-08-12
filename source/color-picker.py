from gpiozero import RGBLED
from time import sleep

led = RGBLED(red=10, green=9, blue=11)
led.color = (1, 1, 1)

# led.red = 0  # full red
# led.color = (1, 0, 1)  # full green
# led.color = (0, 1, 0)  # magenta
# led.color = (0, 0, 1)  # yellow
# led.color = (1, 0, 0)  # cyan
# led.color = (0, 0, 0)  # white


# slowly increase intensity of blue

#for n in range(100):
#    led.blue = n / 100.0
#    led.red = 1 / (n + 1.0)
#    sleep(0.1)


def color(R, G, B):
  led.color = (R, G, B)
#  sleep(2)
#  turnOff()


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


def main():
  while True:
    cmd = raw_input("Choose an option:")

    if cmd == "red on":
      redOn()

    elif cmd == "red off":
      redOff()

    elif cmd == "green on":
      greenOn()

    elif cmd == "green off":
      greenOff()

    elif cmd == "blue on":
      blueOn()

    elif cmd == "blue off":
      blueOff()

    elif cmd == "yellow on":
      yellowOn()

    elif cmd == "yellow off":
      yellowOff()

    elif cmd == "cyan on":
      cyanOn()

    elif cmd == "cyan off":
      cyanOff()

    elif cmd == "magenta on":
      magentaOn()

    elif cmd == "magenta off":
      magentaOff()

    elif cmd == "white on":
      whiteOn()

    elif cmd == "white off":
      whiteOff()

    elif cmd == "off":
	turnOff()

    elif cmd == "shut":
	turnOff()
	return

    else:
      print("Comando no valido.")



  return

# corre el programa
main()
