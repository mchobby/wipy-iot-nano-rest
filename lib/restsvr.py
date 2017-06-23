import ure
import ujson

# A simple REST server API that works pretty well on WiPy 1
# Based on the AiCWebserv.py demo
#
# Developped by Meurisse D. for shop.mchobby.be - CC-BY-SA
#
# Distributed as it, without warranties 
#
# 2017/01/02 - send object returned by action as json dump
# 2017/06/22 - action can also returns ('file:html', html_filename) for static html file   

def send_header( conn, ErrorCode, ErrorMsg, ContentType='text/html' ):
	conn.send( 'HTTP/1.1 ')
	conn.send( str(ErrorCode) )
	conn.send( ' %s\n' % ErrorMsg )
	conn.sendall( 'Connection: close\nServer: nanoRest\nContent-Type: %s\n\n' % ContentType )

def rest_server( actions, debug=True ):
	# minimal rest Webserver. Actions = [ (regex_string, action_callback), ... ]
	# actioncallback will be called with the Match object as parameter
	import socket	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('', 80))
	s.listen(0)	# just queue up some requests
	while True:
		conn, addr = s.accept()
		if debug:
			print("Got a connection from %s" % str(addr))
		request = conn.recv(1024)
		# ignore empty request
		if request == b'':
			if debug:
				print("Connection with %s sharp closed" % str(addr))
			conn.close()
			continue

		# extract the METHOD and URI from request (max 50 chars)
		request = str(request)
		try:
			pos = request.index(" HTTP",0,50)
			method, uri = (request[2:pos]).split()
		except ValueError:
			s = None 
			method, uri = None, None
			if debug:
				print("ValueError for Request content %s" % request )
			send_header( conn, 500, 'Internal Server Error' )
			conn.sendall( "500 Internal Server Error\n" )
			if debug:
				conn.sendall("ValueError for Request content!\n" )
				conn.sendall( request )
			conn.close()
			continue
		
		if debug and method:
			print( "method, uri = %s, %s" % (method,uri) )

		# Simply halt the server on /exit request
		# Only possible in debug mode 
		if debug and uri.find("/exit") >= 0:
			send_header( conn, 200, 'OK' )
			conn.sendall('rest_server exit!\n')
			conn.close()
			return # exit the server

		
		if method != "GET":
			# Method Not Allowed
			send_header( conn, 405, 'Method Not Allowed')
			conn.sendall( "405 Method Not Allowed\n" )
		else:
			try:
				catch = False
				for regexp, action in actions:
					if debug:
						print( "testing re : %s" % regexp )
					m = ure.match( regexp, uri )
					if m:
						catch = True
						if debug:
							print( 'Match!')
						ar = action(m) # call the action and get action result
						# if not a tuple, just returns the object as JSON
						# if tuple, we have ( type_string, data_value )
						if type( ar ) != tuple: 
							#conn.sendall('HTTP/1.1 200 OK\nConnection: close\nServer: nanoWiPy\nContent-Type: application/json\n\n')
							send_header( conn, '200', 'OK', ContentType='application/json')
							conn.sendall( ujson.dumps(ar) )
							break
						elif ar[0] == 'json': # ('json', data_object )
							send_header( conn, '200', 'OK', ContentType='application/json')
							conn.sendall( ujson.dumps(ar[1]) )
						elif ar[0] == 'file:html': # ('file:html', html_filename_with_path )
							send_header( conn, '200', 'OK', ContentType='text/html')
							with open( ar[1], 'r' ) as html_file:
								conn.send( html_file.read() )
							conn.sendall('\n')
						else:
							raise Exception( 'Action returned unhandled %s data type' % ar[0] ) 
				if not catch:
					# Bad request
					send_header( conn, 400, 'Bad request')
					conn.send( "400 Bad request\n" )

			except Exception as e:
				#conn.sendall('HTTP/1.1 500 OK\nConnection: close\nServer: nanoWiPy\nContent-Type: text/html\n\n')
				send_header( conn, 500, 'Internal Server Error' )
				conn.sendall( "500 Internal Server Error\n" )
				if debug:
					conn.send( '%s\n' % e.__class__.__name__ )
					for arg in e.args:
						conn.send( '%r\n' % arg )
		conn.close()
		if debug:
			print("Connection with %s closed" % str(addr))
