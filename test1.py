from gpiozero import RGBLED
from time import sleep

led = RGBLED(red=10, green=9, blue=11)
led.color = (1, 1, 1)

led.red = 0  # full red
sleep(1)
led.red = 0.5  # half red
sleep(1)

led.color = (1, 0, 1)  # full green
sleep(1)
led.color = (0, 1, 0)  # magenta
sleep(1)
led.color = (0, 0, 1)  # yellow
sleep(1)
led.color = (1, 0, 0)  # cyan
sleep(1)
led.color = (0, 0, 0)  # white
sleep(1)


led.color = (1, 1, 1)  # off
sleep(1)

# slowly increase intensity of blue

for n in range(100):
    led.blue = n / 100.0
    led.red = 1 / (n + 1.0)
    sleep(0.1)


led.color = (1, 1, 1)

for n in range(100):
    led.green = n / 100.0
    led.blue = 1 / (n + 1.0)
    sleep(0.1)

led.color = (1, 1, 1)

for n in range(100):
    led.red = n / 100.0
    led.green = 1 / (n + 1.0)
    sleep(0.1)

led.color = (1, 1, 1)
