import RPi.GPIO as GPIO
import threading

GPIO.setmode(GPIO.BCM)		# GPIO has 2 types of numbering system (this one is mainly used)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)		# set pin mode, set pin 5 as an INPUT (3th param is optional)
GPIO.setup(6, GPIO.OUT)		# set pin 6 as an OUTPUT
GPIO.setup(12, OUT)			# WDT (定期的にレベルを反転させる output pin)
GPIO.setup(13, OUT)			# LED brink

state = False				# initialize state as LOW

def SHUT_REQ():
	# シャットダウン処理開始
	GPIO.output(6, GPIO.LOW)	# GPIO.LOW or 0 or False (SUT_ACK)
	# TODO: Run SHUT_DOWN func, if success then output pin 6 as HIGH
	print("TODO: シャットダウン動作")
	# SHUT_ACK
	print("TODO: pin6 をHIGHにする")	
	GPIO.output(6, GPIO.HIGH)	

# 動作状態の判定
def WDT():
	# 4分間に1回 output信号を反転させる
	threading.Timer(5, WDT).start()
	GPIO.output(12, !state)

WDT()

# LED を光らせる
def MODE_LED_REQ():
	GPIO.output(13, GPIO.LOW)	


# Attached Events and callback funtions to pin 5 (it run on separate thread)
# FALLING: When gpio going from high to low
# to remove event
# GPIO.remove_event_detect(5)
GPIO.add_event_detect(5, GPIO.FALLING, callback=SHUT_REQ, bouncetime=300)

# If dont cleanup, GPIO will remain in the last set state
GPIO.cleanup()