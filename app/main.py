def application(env, start_resp):
	start_resp('200', [('Content-Type', 'text/plain')])
	return ['<b>Hello, WSGI!</b>'.encode('utf-8')]
