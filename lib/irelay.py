from machine import Pin

# GPIO & PINs attach to relay 1..N
RELAY_GPIO  = ['GP11','GP12','GP13', 'GP14']
RELAY_PIN   = [] # Will retain the Pin object  
RELAY_STATE = [] # Will retain the last Pin state

# Use this declaration when the relay is activated by a HIGH signal
# RELAY_ON,RELAY_OFF = 1, 0
# Use this declaration when the relay is activated by a LOW signal
RELAY_ON,RELAY_OFF = 0, 1

def init_relay_gpio():
	""" Initialize the relay GPIO """  
	for gpio in RELAY_GPIO:
		RELAY_PIN.append( Pin(gpio,mode=Pin.OUT ))
		# Disable the relay
		RELAY_PIN[-1].value( RELAY_OFF )
		# REmember the state
		RELAY_STATE.append( False ) # False state for OFF

def update_relay( match ):
	""" rest_server callback: Update the target relay. """ 
	# match: is the ure.Match object resulting from re
	# returns: an object that will be dump in json
	
	#print( 'Set the relay %s to %s' % (match.group(1), match.group(2)) )
	nrelay = int( match.group(1) ) # relay number from 1..N
	state  = match.group(2)        # on/off

	pin = RELAY_PIN[nrelay-1] # the list goes from 0 to N-1
	pin.value( RELAY_ON if state=='on' else RELAY_OFF )
	# Remember the state
	RELAY_STATE[nrelay-1] = True if state=='on' else False
	# Return the state a s confirmation
	return RELAY_STATE[nrelay-1]

def relay_state( match ):
	""" rest_server callback: return the current state of the relay """
	nrelay = int( match.group(1) ) # relay number from 1..N
	return RELAY_STATE[nrelay-1]

def relay_states( match ):
	""" rest_server callback: return the state of all the relays """
	# Getting [ (relaynr,state),(relaynr,state),... ]
	_r = zip( range(1,len(RELAY_GPIO)+1) , RELAY_STATE )
	# Transform into dict.
	# The dict key must be a string if you want to reload the json in python 
	_d = {}
	for k,v in _r:
		_d['relay%s'%k]=v
	return _d

def index_page( match ):
	return ( 'file:html', 'wipy-relay.html' )
    
# Define supported action (via Regular Expression) and action_callback to call
irelay_actions = [ ( "^\/relay\/([1-4])\/(on|off)$", update_relay),
	( "^\/relay\/([1-4])\/$", relay_state ),
	( "^\/relay\/$", relay_states),
	( "^\/$", index_page ) ]


init_relay_gpio()

# Start the Rest server with
#   from restsvr import rest_server
#   rest_server( irelay_actions, debug=True )
