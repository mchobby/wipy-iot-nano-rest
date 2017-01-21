from machine import Pin
from restsvr import rest_server

# AutoStart the REST Server (when forced to GND)
AUTOSTART_GPIO = 'GP8'

def is_auto_start():
	""" Check the AutoStart Pin. Pull it down to automatically
	    start the Rest Server """
	auto_pin = Pin( AUTOSTART_GPIO, mode=Pin.IN, pull=Pin.PULL_UP )
	return auto_pin.value()==0

# Init the relay GPIO
# defines the irelay_actions = [(regex,callback_method)]
from irelay import *

# Allows to restart the WiPy without activating the Rest Server.
# Disabling Rest server will enable/autorise Telnet/ftp sessions on the WiPy
if is_auto_start():
	# Using debug print out additionnal message and allows /exit on the rest_server 
	# rest_server( actions, debug=True )
	rest_server( irelay_actions, debug=False )
