
import socket
import threading

def receive_messages(sock):
    """Hilo que recibe mensajes del servidor."""
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print("Servidor desconectado.")
                break
            print("\nServidor:", data.decode('utf-8'))
        except:
            break

def start_client():
    host = 'localhost'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    try:
        client_socket.connect((host, port))
        print(f"Conectado al servidor en {host}:{port}")
        print("Escribe tus mensajes. Escribe 'salir' para terminar.")
        # Hilo para recibir mensajes del servidor
        threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

        while True:
            msg = input("Tú: ")
            if msg.lower() == "salir":
                break
            client_socket.send(msg.encode('utf-8'))
    except ConnectionRefusedError:
        print("No se pudo conectar al servidor. Asegúrate de que esté ejecutándose.")
    except socket.error as e:
        print(f"Error de socket: {e}")
    finally:
        client_socket.close()
        print("Cliente cerrado.")

if __name__ == "__main__":
    start_client()
