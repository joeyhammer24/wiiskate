# Created By: Joey Hammer
# Credit to Brian Hensley, The Raspberry Pi Guy, and Tim Maier
# Date:        4/7/2021
# Version 1
#-------------------------------------------------------------------------------

import cwiid
import time
import RPi.GPIO as GPIO

def main():

	print 'Press button 1 + 2 on your Wii Remote...'

	while True:
	    try:
		wm=cwiid.Wiimote()
		break
	    except:
		pass
	wm.rpt_mode = cwiid.RPT_BTN


	print 'Wii Remote connected...'
	print '\nPress the HOME button to disconnect the Wii and end the application'

	Rumble = False
        wm.rpt_mode = cwiid.RPT_BTN
	wm.led=1

	d = 50						#initial duty cycle 50%
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(12, GPIO.OUT)
	GPIO.setup(16, GPIO.OUT)
	pwm=GPIO.PWM(12,1000)				#(pin, frequency Hz)



	while True:

		if wm.state['buttons'] == 2048:
			print ('Increase duty cycle', d)
			d=d+10
			time.sleep(.2)
			if d > 100:
				d=100

		if wm.state['buttons'] == 1024:
			print ('Decrease duty cycle', d)
			d=d-10
			time.sleep(.2)
			if d < 0:
				d=0

		if wm.state['buttons'] == 2052:
			print ('Increase duty cycle', d)
			d=d+10
			time.sleep(.2)
			if d > 100:
				d=100

		if wm.state['buttons'] == 1028:
			print ('Decrease duty cycle', d)
			d=d-10
			time.sleep(.2)
			if d < 0:
				d=0

		if wm.state['buttons'] == 256:
			print 'LEFT'
			time.sleep(.5)

		if wm.state['buttons'] == 512:
			print 'RIGHT'
			time.sleep(.5)

		if wm.state['buttons'] == 8:
			print 'A'
			GPIO.output(16,GPIO.HIGH)
			time.sleep(.25)

		if wm.state['buttons'] == 4:
			print 'B'
			pwm.start(d)
			time.sleep(.2)

		if wm.state['buttons'] == 2:
			print '1'
			time.sleep(.5)

		if wm.state['buttons'] == 1:
			print '2'
			time.sleep(.5)

		if wm.state['buttons'] == 4096:
			print 'PLUS+'
			time.sleep(.5)

		if wm.state['buttons'] == 16:
			print 'MINUS-'
			time.sleep(.5)

		if wm.state['buttons'] == 128:
			print 'closing Bluetooth connection. Good Bye!'
			time.sleep(1)
			exit(wm)

if __name__ == '__main__':
    main()
GPIO.cleanup()
