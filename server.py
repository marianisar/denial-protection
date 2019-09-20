#############################################################################
#                                                                           #
#                       Copyright 2019 MARIA NISAR.                         #
#                           All Rights Reserved.                            #
#                                                                           #
#                                                                           #
#############################################################################
'''
Created on SEP 16, 2019

@author: Maria Nisar
'''


from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from threading import Thread
import cgi
import sys
import time


class ThreadedHTTPServer(HTTPServer):
    def process_request(self, request, client_address):
        thread = Thread(target=self.__new_request, args=(self.RequestHandlerClass, request, client_address, self))
        thread.start()
    def __new_request(self, handlerClass, request, address, server):
        handlerClass(request, address, server)
        self.shutdown_request(request)

class Handler(BaseHTTPRequestHandler):

    clients=0
    client_requests=dict()
    time=5
    requests=5

    def do_GET(self):
        id = int((self.path).split('=')[1])
        if (self.clients <= 0):
            res = 'No Client is Simulated \n'
            sys.stdout.write(str(res))
            self.wfile.write(str(res))

        elif (id > self.clients):
            res = 'Invalid Id \n'
            sys.stdout.write(str(res))
            self.wfile.write(str(res))

        else:
            now = time.time()
            if (self.client_requests.get(id)==None):
                self.client_requests[id]=list()
                self.client_requests[id].append(1)
                self.client_requests[id].append(now)
                self.send_response(200)
                sys.stdout.write('200 OK\n')

            while(True):
                if((now-self.client_requests[id][1])<self.time and self.client_requests[id][0]>=self.requests):
                    self.send_response(503)
                    sys.stdout.write('503 Service Unavailable\n')
                    time.sleep(now-self.client_requests[id][1])
                elif((now-self.client_requests[id][1])>self.time) :
                    self.client_requests[id][0]=1
                    self.client_requests[id][1]=now
                    self.send_response(200)
                    sys.stdout.write('200 OK\n')
                else:
                    val=self.client_requests[id][0]
                    self.client_requests[id][0] +=1
                    self.send_response(200)
                    sys.stdout.write('200 OK\n')
                now = time.time()

    def do_POST(self):

        form=cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )
        self.send_response(200)
        self.end_headers()

        user_id=int(form.getvalue('user_id'))
        if(user_id>0):
            Handler.clients=user_id
            res="{0} : HTTP clients simulate ".format(user_id)
        else:
            res='Please Enter valid Client number'


        sys.stdout.write(str(res) + '\n')

        self.wfile.write(str(res))


try:

    server = ThreadedHTTPServer(('localhost', 8080), Handler)
    while True:
        server.handle_request()

except KeyboardInterrupt:
	print 'Shutting down the web server'
	server.socket.close()