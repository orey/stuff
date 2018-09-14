import socket, sys
import http.server
import socketserver

DEFAULTPORT = 8081

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    myip = s.getsockname()[0]
    s.close()
    print("=========================")
    print("Your IP address is: " + myip)
    print("=========================")
    print("Simplest web server")
    port = DEFAULTPORT
    if len(sys.argv) == 2:
        try:
            port = int(sys.argv[1])
        except Exception:
            print("Usage: ")
            print("$ python3 server.py [port]")
            print("Note: port is optional")
            port = DEFAULTPORT
            print("Defaulting on port ", port)
    else: 
        print("Default port = " + str(port))
    Handler = http.server.SimpleHTTPRequestHandler
    socketserver.TCPServer(("", port), Handler).serve_forever()


