# 1200015, 1200275, 1200779
#TCP WEB SERVER
from socket import*
# Create a TCP socket
Websock = socket(AF_INET, SOCK_STREAM)
# Declare host name and its port
HOST_NAME = 'localhost'
HOST_PORT = 7788
# Bind the socket to a local address and port
Websock.bind((HOST_NAME, HOST_PORT))
print("The server is ready!!\n")
# Start listening for incoming connections
Websock.listen(1)

while True:
    # Accept an incoming connection
    conn, addr = Websock.accept()
    # Receive data from the client
    sentence = conn.recv(1024).decode()
    #Client ip
    ip = addr[0]
    # Client port
    port = addr[1]
    #To display the request on the terminal
    print(sentence)
    #print('\n')
    # Parse the received data to determine the request method, path, and any additional headers
    method, path, version = sentence.split()[0:3]
    #print(method)
    #print('\n')
    #print(addr)
    #print(path)
    #print(version)
    #To check if the method is as demand
    if method == "GET":
        # To check the path and then Send English page
        if path in ["/", "/en", "/index.html", "/main_en.html", "/.html"]:
            # Send the HTTP response
            # To send the status line
            conn.send("HTTP/1.1 200 OK\r\n".encode())
            # To send the header lines
            conn.send("Content-Type: text/html\r\n".encode())
            conn.send("\r\n".encode())
            #Open the requested file
            f1 = open("main_en.html", "rb")
            #To send the requested data (html file)
            conn.send(f1.read())
            #Close the file
            f1.close()
            continue
        # To check the path and then Send Arabic page
        elif path in ["/ar", "/main_ar.html"]:
            # Send the HTTP response
            # To send the status line
            conn.send("HTTP/1.1 200 OK\r\n".encode())
            # To send the header lines
            conn.send("Content-Type: text/html\r\n".encode())
            #To make the arabic language accepted
            conn.send("charset: utf-8\r\n".encode())
            conn.send("\r\n".encode())
            # Open the requested file
            f1 = open("main_ar.html", "rb")
            # To send the requested data (html file)
            conn.send(f1.read())
            # Close the file
            f1.close()
            continue
        # To check the path and then Send English CSS File
        elif path == "/.css":
            # Send the HTTP response
            # To send the status line
            conn.send("HTTP/1.1 200 OK\r\n".encode())
            # To send the header lines
            conn.send("Content-Type: text/css\r\n".encode())
            conn.send("\r\n".encode())
            # Open the requested file
            f1 = open("main_en.css", "rb")
            #To send the requested file
            conn.send(f1.read())
        # To check the path and then Send png image
        elif path == "/.png":
            # Send the HTTP response
            # To send the status line
            conn.send("HTTP/1.1 200 OK\r\n".encode())
            # To send the header lines
            conn.send("Content-Type: image/png\r\n".encode())
            conn.send("\r\n".encode())
            # Open the requested file
            f1 = open("image.png", "rb")
            # To send the requested file
            conn.send(f1.read())
        # To check the path and then Send jpg image
        elif path == "/.jpg":
            # Send the HTTP response
            # To send the status line
            conn.send("HTTP/1.1 200 OK\r\n".encode())
            # To send the header lines
            conn.send("Content-Type: image/jpg\r\n".encode())
            conn.send("\r\n".encode())
            # Open the requested file
            f1 = open("background.jpg", "rb")
            # To send the requested file
            conn.send(f1.read())
        #To get the style of English page and send it to the client
        elif path == "/main_en.css":
            conn.send("HTTP/1.1 200 OK\r\n".encode())
            conn.send("Content-Type: text/css\r\n".encode())
            conn.send("\r\n".encode())
            f1 = open("main_en.css", "rb")
            conn.send(f1.read())
            f1.close()
            continue
        #To get the background of English & Arabic pages and send it to the client
        elif path == "/Fordesc.jpg":
            conn.send("HTTP/1.1 200 OK\r\n".encode())
            conn.send("Content-Type: image/jpg\r\n".encode())
            conn.send("\r\n".encode())
            f1 = open("Fordesc.jpg", "rb")
            conn.send(f1.read())
            f1.close()
            continue
        #To get the logo of English & Arabic page and send it to the client
        elif path == "/bzu.png":
            conn.send("HTTP/1.1 200 OK\r\n".encode())
            conn.send("Content-Type: image/png\r\n".encode())
            conn.send("\r\n".encode())
            f1 = open("bzu.png", "rb")
            conn.send(f1.read())
            f1.close()
            #continue
            # To get the style of Arabic page and send it to the client
        elif path == "/main_ar.css":
            conn.send("HTTP/1.1 200 OK\r\n".encode())
            conn.send("Content-Type: text/css\r\n".encode())
            conn.send("\r\n".encode())
            f1 = open("main_ar.css", "rb")
            conn.send(f1.read())
            f1.close()
            continue
        # To redirect the request to google website
        elif path == "/go":
            # Send the HTTP response
            # To send the status line
            conn.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
            # To send the location or destination
            conn.send("Location: http://www.google.com\r\n".encode())
            conn.send("\r\n".encode())
        # To redirect the request to stackoverflow website
        elif path == "/so":
            conn.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
            conn.send("Location: https://stackoverflow.com/\r\n".encode())
            conn.send("\r\n".encode())
        # To redirect the request to bzu main website
        elif path == "/bzu":
            conn.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
            conn.send("Location: https://www.birzeit.edu/ar\r\n".encode())
            conn.send("\r\n".encode())
        # If the request not found
        else:
            # Declare a String of html code
            error = """<!DOCTYPE html>
            <html lang=\"en\">
            <head>
            <meta charset=\"UTF-8\">
            <title>Error</title>
            </head>
            <body>
            <h1 style=\"color: red;\">The file is not found</h1>
            <p><b>Firas Sandouka 1200779 ~~~ Mahmoud Khatib 1200275 ~~~~ Abdalkarim Eiss 1200015</b></p></body></html>"""
            # Send the HTTP response
            # To send the status line
            conn.send("HTTP/1.1 404 Not Found\r\n".encode())
            conn.send("Content-Type: text/html\r\n".encode())
            conn.send("\r\n".encode())
            # To send the html code as bytes
            conn.send(error.encode())
            # To display the ip and port of client on the body
            conn.send(f'IP: ({ip}) ~~~~ Port: ({port})'.encode())
    #To close the connection
    conn.close()
# To close the socket
Websock.close()
