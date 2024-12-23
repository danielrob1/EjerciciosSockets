import socket

def servidor_udp_broadcast():
    # Crear socket UDP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.bind(("", 5000))
    print("[SERVIDOR] Escuchando mensajes en broadcast en el puerto 5000...")
     # Recibir datos del cliente
    datos, addr = s.recvfrom(1024)
    print(f"[SERVIDOR] Mensaje recibido de {addr}: {datos.decode()}")
    respuesta = "Mensaje recibido"
    s.sendto(respuesta.encode(), ("192.168.56.255", 5000))
    print(f"[SERVIDOR] Respuesta enviada en broadcast.")

servidor_udp_broadcast()
