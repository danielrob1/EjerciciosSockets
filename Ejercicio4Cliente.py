import socket

def cliente_tcp():
    # Crear socket
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Intentar conectar al servidor
        c.connect(("127.0.0.1", 5000))
        print("[CLIENTE] Conectado al servidor.")
        # Recibir mensaje del servidor
        msg = c.recv(1024)
        print("[CLIENTE] Mensaje del servidor:", msg.decode())
        # Enviar una respuesta al servidor
        respuesta = "Hola servidor, aquí el cliente!"
        c.send(respuesta.encode())
        # Recibir la respuesta del servidor
        msg = c.recv(1024)
        print("[CLIENTE] Mensaje del servidor:", msg.decode())
    except (socket.error, Exception) as e:
        print(f"[CLIENTE] Error: {e}")
    finally:
        # Cerrar el socket
        c.close()
        print("[CLIENTE] Conexión cerrada.")

cliente_tcp()
