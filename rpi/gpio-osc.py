# External module imports
import RPi.GPIO as GPIO
import time

# Pin Definitons:
button1 = 3
button2 = 5
button3 = 7
button4 = 11
button5 = 13
button6 = 15
button7 = 19
button8 = 21
buttonRecord = 23

# Pin Setup:
GPIO.setmode(GPIO.BOARD) # Broadcom pin-numbering scheme
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
GPIO.setup(button4, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
GPIO.setup(button5, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
GPIO.setup(button6, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
GPIO.setup(button7, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
GPIO.setup(button8, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
GPIO.setup(buttonRecord, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up

print("Here we go! Press CTRL+C to exit")
try:
	while True:
            if GPIO.input(button1) == False:
        	print('Button 1 Pressed')
        	time.sleep(0.2)
            elif GPIO.input(button2) == False:
        	print('Button 2 Pressed')
        	time.sleep(0.2)
            elif GPIO.input(button3) == False:
        	print('Button 3 Pressed')
        	time.sleep(0.2)
            elif GPIO.input(button4) == False:
        	print('Button 4 Pressed')
        	time.sleep(0.2)
            elif GPIO.input(button5) == False:
        	print('Button 5 Pressed')
        	time.sleep(0.2)
            elif GPIO.input(button6) == False:
        	print('Button 6 Pressed')
        	time.sleep(0.2)
            elif GPIO.input(button7) == False:
        	print('Button 7 Pressed')
        	time.sleep(0.2)
            elif GPIO.input(button8) == False:
        	print('Button 8 Pressed')
        	time.sleep(0.2)
            elif GPIO.input(buttonRecord) == False:
        	print('Button Record Pressed')
        	time.sleep(0.2)

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO
