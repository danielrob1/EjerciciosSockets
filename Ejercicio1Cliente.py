import socket

def cliente_tcp():
    # Crear socket
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(("127.0.0.1", 5000))
    print("[CLIENTE] Conectado al servidor.")

    # Recibir mensaje del servidor
    #msg = c.recv(1024)
    #print("[CLIENTE] Mensaje del servidor:", msg.decode())

    # Enviar una respuesta
    respuesta = "Hola servidor, aquí el cliente!"
    c.send(respuesta.encode())

    msg=c.recv(1024)
    print("[CLIENTE] Mensaje del servidor:", msg.decode())


    c.close()
    print("[CLIENTE] Conexión cerrada.")

# Ejecuta esta celda en otro entorno después de haber lanzado el servidor.
cliente_tcp()