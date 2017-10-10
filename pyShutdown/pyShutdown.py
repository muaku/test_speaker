import RPi.GPIO as GPIO
import threading
import subprocess
import signal
from time import sleep

GPIO.setmode(GPIO.BCM)		# GPIO has 2 types of numbering system (this one is mainly used)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)		# set pin mode, set pin 5 as an INPUT (3th param is optional)
GPIO.setup(6, GPIO.OUT)		# set pin 6 as an OUTPUT
GPIO.setup(12, GPIO.OUT)			# WDT 
GPIO.setup(13, GPIO.OUT)			# LED brink

state = False				# initialize state as LOW

def SHUT_REQ():
	# Start shutdown process
	GPIO.output(6, GPIO.LOW)	# GPIO.LOW or 0 or False (SUT_ACK)
	sleep(1)
	# TODO: Run SHUT_DOWN func
	print("TODO: Shutdown process")
	shutdown()

# Shutdown
def shutdown():
	command = "/usr/bin/sudo /sbin/shutdown -h now"			# -h: halt the system
	process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
	output = process.communicate()[0]
	print(output)
	

# Observe state
def WDT():
	#  ouput 4min per 1 time
	global state
	if state:
		state = False
	else:
		state = True
	threading.Timer(240, WDT).start()
	GPIO.output(12, state)
	print(state)

WDT()

# LED bright
def MODE_LED_REQ():
	GPIO.output(13, GPIO.LOW)	

# Restart
def restart():
	command = "/usr/bin/sudo /sbin/shutdown -r now"
	process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
	output = process.communicate()[0]
	print (output)

# test: shutdown when reach 10 sec
# signal.signal(signal.SIGALRM, shutdown)
# signal.alarm(10)

# Attached Events and callback funtions to pin 5 (it run on separate thread)
# FALLING: When gpio going from high to low
# to remove event
# GPIO.remove_event_detect(5)
GPIO.add_event_detect(5, GPIO.FALLING, callback=SHUT_REQ, bouncetime=300)

# If dont cleanup, GPIO will remain in the last set state
GPIO.cleanup()

