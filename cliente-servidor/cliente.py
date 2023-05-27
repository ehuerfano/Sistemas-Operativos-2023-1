import socket

def send_message(message):
    host = 'localhost'
    port = 8888

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))  # Conectar al servidor

    client_socket.send(message.encode())  # Enviar mensaje al servidor
    response = client_socket.recv(1024)  # Recibir respuesta del servidor
    print(f'Respuesta del servidor: {response.decode()}')

    client_socket.close()  # Cerrar el socket del cliente

# Ejemplo de uso del cliente
send_message('Hola, servidor!')
