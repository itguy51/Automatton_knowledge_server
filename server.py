from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import urlparse
import json
from main import *

#This is just a basic web server for automatton
class Automatton_Handler(BaseHTTPRequestHandler):
    #THIS IS NEEDED, DO NOT GET RID OF THIS
    #IT WILL THROW AN ERROR
    global query
    def do_GET(self):
        self.send_response(200)
        #We send json data, so make sure the browser knows that
        self.send_header("Content-type", "application/json")
        self.end_headers()

        #We need to get the query, so parse the url
        qs = {}
        path = self.path
        if '?' in path:
            path, tmp = path.split('?', 1)
            qs = urlparse.parse_qs(tmp)
            query = qs["query"][0]

        #Calculate query
        calc_response = bw.interpret(query)

        #Write json data of computation
        self.wfile.write(json.dumps(calc_response))

        return

    def log_request(self, code=None, size=None):
        print "Request"

    def log_message(self, format, *args):
        print "I don't know what this is."

if __name__ == "__main__":
    try:
        server = HTTPServer(('localhost', 2092), Automatton_Handler)
        print "Automatton knowledge server running on port: 2092"
        server.serve_forever()
    except KeyboardInterrupt:
        print "^C recieved, shutting down server"
        server.socket.close()

