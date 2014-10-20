import pifacedigitalio
import time

pf = pifacedigitalio.PiFaceDigital()
while True:
	for led in range(0, 8):
		for led2 in range(0, 8):
			pf.leds[led2].turn_off()
		pf.leds[led].turn_on()
#		time.sleep(0.25)

