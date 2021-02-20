import socket
import os  # mainly used to find path of file
import mimetypes # to get the content-type
class HTTPserver:
    """this method parse incoming request header and handle the GET request accordingly"""
    def parse_HTTPrequest(self,request):
        # split all line breaks
        lines = request.split(b"\r\n")
        # split to get method , URI , HTTP version
        words = lines[0].split(b" ")
        if len(lines) > 2:
            self.method = words[0].decode()
            self.uri = words[1].decode()
            self.httpversion = words[2].decode()
            print(words[0].decode() + " " + words[1].decode() + " " + words[2].decode())

    def handle_GET(self,request):
       self.parse_HTTPrequest(request)
       path = self.uri.strip('/')  # remove slash from URI
       if bool(path) == False: #empty path is False
            #An empty path means client is at the homepage therefore this is the default path
            path = 'server.html' #default html file
       #handle 200
       if os.path.exists(path):
           response_line = b'HTTP/1.1 200 OK \r\n'
           content_type = mimetypes.guess_type(path)[0].encode() or b'text/html'
           response_headers = b'Server: PankcakeServer\r\n' + b'content-type: ' + content_type + b'\r\n'
           blank_line = b'\r\n'
           with open(path, 'rb') as f:
               response_body = f.read()
       #handle 404
       else:
           response_line = b'HTTP/1.1 404 Not Found \r\n'
           response_headers = b'Server: PankcakeServer\r\n'
           response_body = b'<h1><center>404 Not Found</center></h1>'
           blank_line = b'\r\n'

       response = b''.join([response_line, response_headers, blank_line, response_body])
       return response

# Create socket
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((SERVER_HOST, SERVER_PORT))
    s.listen(5)
    print(f'Listening on port {SERVER_PORT} ...')
    #wait for incoming client
    while True:
        client, client_address = s.accept()
        print(f"{client_address} has connected!")
        # Get the client request
        with client as c:
            request = c.recv(1024)
            #instantiate object from HTTPserver class
            server = HTTPserver()
            c.sendall(server.handle_GET(request))
            c.close()
