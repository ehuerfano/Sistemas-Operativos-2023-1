import socket
import threading

def handle_client(client_socket):
    # Manejar la comunicación con un cliente específico
    while True:
        data = client_socket.recv(1024)  # Recibir datos del cliente
        if not data:
            break  # Si no hay más datos, salir del bucle
        response = data.upper()  # Ejemplo de procesamiento: convertir a mayúsculas
        client_socket.send(response)  # Enviar respuesta al cliente
    client_socket.close()  # Cerrar el socket del cliente

def start_server():
    host = 'localhost'
    port = 8888

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)  # Escuchar conexiones entrantes

    print(f'Servidor escuchando en {host}:{port}')

    while True:
        client_socket, address = server_socket.accept()  # Aceptar una nueva conexión
        print(f'Cliente conectado desde {address[0]}:{address[1]}')
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()  # Iniciar un nuevo hilo para manejar al cliente

start_server()
