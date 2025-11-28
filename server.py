
import socket
import threading



def handle_client_receive(client_socket):
    """Hilo que recibe mensajes del cliente."""
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                print("Cliente desconectado.")
                break
            message = data.decode('utf-8')
            print(f"Cliente: {message}")

        except ConnectionResetError:
            print("La conexión fue cerrada forzosamente por el cliente.")

            break



def start_server():
    host = 'localhost'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server_socket.bind((host, port))
        print(f"Servidor iniciado en {host}:{port}")
    except socket.error as e:
        print(f"Error al vincular el socket: {e}")
        return
    
    server_socket.listen(1)
    print(f"Servidor escuchando en {host}:{port}")
    print("Esperando conexiones...")

    client_socket, addr = server_socket.accept()
    print(f"Cliente conectado desde {addr}")

    # Hilo para recibir mensajes
    threading.Thread(target=handle_client_receive, args=(client_socket,), daemon=True).start()

    # Enviar mensajes desde el servidor
    try:
        while True:
            msg = input("Servidor: ")
            if msg.lower() == "salir":
                break
            client_socket.send(msg.encode('utf-8'))
    except ConnectionRefusedError:
        print("No se pudo conectar al servidor. Asegúrate de que esté ejecutándose.")
    finally:
        client_socket.close()
        server_socket.close()
        print("Servidor cerrado.")

if __name__ == "__main__":
    start_server()











