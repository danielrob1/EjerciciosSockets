import socket

def cliente_tcp():
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(("127.0.0.1", 5000))
    print("[CLIENTE] Conectado al servidor.")

    while True:
        mensaje = input("Escribe un mensaje (QUIT para salir): ")
        c.send(mensaje.encode())
        if mensaje == "QUIT":
            print("[CLIENTE] Conexión cerrada por el cliente.")
            break

        respuesta = c.recv(1024)
        print("[CLIENTE] Respuesta del servidor:", respuesta.decode())

    c.close()

cliente_tcp()
