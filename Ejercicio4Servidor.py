import socket
def servidor_tcp():
    # Crear socket TCP IPv4
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Configurar y escuchar en el puerto 5000
        s.bind(("127.0.0.1", 5000))
        s.listen(1)  # Aceptar una conexión
        print("[SERVIDOR] Esperando conexiones...")
        # Aceptar conexión entrante
        conn, addr = s.accept()
        print("[SERVIDOR] Conexión establecida con", addr)
        # Enviar un mensaje al cliente
        mensaje = "Bienvenido al servidor. Envíame algo!"
        conn.send(mensaje.encode())
        # Recibir respuesta del cliente
        datos = conn.recv(1024)
        print("[SERVIDOR] Datos recibidos:", datos.decode())
        # Modificar y enviar la respuesta al cliente
        datos = datos.decode().upper()
        conn.send(datos.encode())
    except (socket.error, Exception) as e:
        print(f"[SERVIDOR] Error: {e}")
    finally:
        # Cerrar la conexión del cliente y del servidor
        conn.close()
        print("[SERVIDOR] Conexión con el cliente cerrada.")
        s.close()
        print("[SERVIDOR] Conexión del servidor cerrada.")


servidor_tcp()
