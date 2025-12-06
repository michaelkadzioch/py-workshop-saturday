import socket

serverHost = '127.0.0.1'  
serverPort = 40444   

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((serverHost, serverPort))
    s.listen()
    print(f'Server lauscht auf {serverHost}:{serverPort}...')

    conn, addr = s.accept()

    with conn:
        print(f'Verbindung von {addr} hergestellt...')

        while True:
            data = conn.recv(1024)
            if not data:
                break

            print(f'Empfangen vom Client: {data.decode('utf-8')}')
            
            response = "Hallo Client, ich habe deine Nachricht erhalten!"

            conn.sendall(response.encode('utf-8'))
            print(f'Gesendet an Client: {response}')

        print(f'Verbindung zu {addr} geschlossen.')