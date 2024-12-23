import socket

def servidor_tcp():
    # Crear socket TCP IPv4
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 5000))
    s.listen(1)  # Aceptar una conexión
    print("[SERVIDOR] Esperando conexiones...")
    conn, addr = s.accept()
    print("[SERVIDOR] Conexión establecida con", addr)

    # Enviar un mensaje al cliente
    mensaje = "Bienvenido al servidor. Envíame algo!"
    conn.send(mensaje.encode())

    # Recibir respuesta del cliente
    datos = conn.recv(1024)
    print("[SERVIDOR] Datos recibidos:", datos.decode())
    datos= datos.decode().upper()

    conn.send(datos.encode())

    conn.close()
    s.close()
    print("[SERVIDOR] Conexión cerrada.")

# Ejecuta esta celda para iniciar el servidor.
# Luego, en otra terminal o en otro notebook, puedes conectar con un cliente.
servidor_tcp()