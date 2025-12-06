import socket

serverHost = '127.0.0.1'  
serverPort = 40444   

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((serverHost, serverPort))

    message = "Hallo Server, ich bin der Client!"

    s.sendall(message.encode('utf-8'))
    
    print(f'Gesendet an Server: {message}')

    data = s.recv(1024)
    print(f'Empfangen vom Server: {data.decode('utf-8')}')