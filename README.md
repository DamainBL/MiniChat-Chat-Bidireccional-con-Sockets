#  MiniChat-Chat-Bidireccional-con-Sockets
es una aplicación simple de mensajería en consola que utiliza sockets TCP y multithreading para permitir comunicación bidireccional en tiempo real entre un servidor y un cliente.

## Características

- Comunicación en tiempo real entre cliente y servidor.
- Envío y recepción simultánea de mensajes gracias al uso de **hilos**.
- Implementación de sockets TCP usando `socket.AF_INET` y `socket.SOCK_STREAM`
---
## Estructura del Proyecto

    PyMiniChat/
    │── server.py # Servidor que recibe y envía mensajes
    │── client.py # Cliente que se conecta al servidor
    └── README.md

---

## Uso

Una vez ambos programas están corriendo:

Lo que escribas en server.py aparecerá en el cliente.

Lo que escribas en client.py aparecerá en el servidor.

Ambos pueden escribir al mismo tiempo gracias al manejo de hilos.

Para salir, escribe: salir

## Cómo Funciona

* Comunicación TCP

El servidor abre un socket en localhost:12345 y se queda "escuchando".
Cuando un cliente se conecta, el servidor crea un socket dedicado para esa conexión.

* Multithreading

Tanto en el servidor como en el cliente:

    def receive_messages(socket):
        while True:
            try:
                data = sock.recv(1024)
                if not data:
                    print("Servidor/cliente desconectado.")
                    break
                print("\nServidor/cliente:", data.decode('utf-8'))
            except:
                break

Un hilo escucha mensajes entrantes.

    threading.Thread(target=receive_messages, args=(client_socket,), daemon=True).start()

El hilo principal lee lo que escribe el usuario y lo envía.
    
     msg = input("Tú: ")
     if msg.lower() == "salir":
        break
     client_socket.send(msg.encode('utf-8'))

Esto permite comunicación bidireccional en simultáneo.


