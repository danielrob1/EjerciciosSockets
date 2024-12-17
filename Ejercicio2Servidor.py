import socket
import threading

def manejar_cliente(conn, addr):
    """Función para manejar la comunicación con un cliente."""
    print(f"[HILO] Conexión aceptada desde {addr}")
    activo = True  # Variable explícita para mantener el bucle activo
    try:
        # Enviar mensaje al cliente
        conn.send(b"Hola, cliente con hilos!\n")

        # Recibir datos del cliente
        while activo:
            datos = conn.recv(1024)
            if datos.decode()!="QUIT":
                print(f"[HILO] Mensaje recibido de {addr}: {datos.decode()}")
                conn.send(b"Mensaje recibido\n")
            else:
                print(f"[HILO] Cliente {addr} desconectado.")
                activo = False  # Finalizar el bucle si no hay más datos
    except Exception as e:
        print(f"[HILO] Error con el cliente {addr}: {e}")
    finally:
        # Cerrar la conexión
        print(f"[HILO] Cerrando conexión con {addr}")
        conn.close()

def servidor_tcp_hilos():
    """Servidor TCP que maneja múltiples clientes con hilos."""
    # Crear socket TCP IPv4
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(("127.0.0.1", 5000))
    servidor.listen(5)  # Poner el servidor en escucha
    print("[SERVIDOR] Escuchando en 127.0.0.1:5000")

    while True:
        # Aceptar una conexión
        conn, addr = servidor.accept()
        print(f"[SERVIDOR] Conexión recibida de {addr}")

        # Crear un hilo para manejar al cliente
        hilo = threading.Thread(target=manejar_cliente, args=(conn, addr))
        hilo.start()  # Iniciar el hilo
        print(f"[SERVIDOR] Hilo iniciado para {addr}")

# Ejecuta esta celda para iniciar el servidor con hilos.
servidor_tcp_hilos()