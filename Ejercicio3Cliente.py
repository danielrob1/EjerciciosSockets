import socket
import time

def cliente_udp_broadcast():
    # Crear socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("", 5000))

    # Direccion del broadcast
    broadcast_addr = ("192.168.56.255", 5000)

    # Enviar un mensaje de broadcast
    mensaje = "Mensaje de broadcast desde el cliente"
    print(f"[CLIENTE] Enviando mensaje de broadcast: {mensaje}")
    s.sendto(mensaje.encode(), broadcast_addr)
    # Establecer tiempo de espera para recibir respuestas
    s.settimeout(3)
    print("[CLIENTE] Esperando respuestas...")
    while True:
        try:
            # Recibir respuestas de servidores
            datos, addr = s.recvfrom(1024)
            print(f"[CLIENTE] Respuesta recibida de {addr}: {datos.decode()}")
        except socket.timeout:
            print("[CLIENTE] Tiempo de espera agotado. No se recibirán más respuestas.")
            break  # Salir del bucle si el tiempo de espera se agota
        except Exception as e:
            print(f"[CLIENTE] Error al recibir respuesta: {e}")
            break
    # Cerrar el socket
    s.close()
    print("[CLIENTE] Conexión cerrada.")
cliente_udp_broadcast()
