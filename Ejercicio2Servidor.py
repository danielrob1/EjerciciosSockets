import socket
import threading

def manejar_cliente(conn, addr):
    print(f"[HILO] Conexión aceptada desde {addr}")
    try:
        while True:
            datos = conn.recv(1024).decode()
            if datos.strip().upper() == "QUIT":
                print(f"[HILO] Cliente {addr} desconectado.")
                break
            respuesta = datos.upper()
            conn.send(respuesta.encode())
    except Exception as e:
        print(f"[HILO] Error con el cliente {addr}: {e}")
    finally:
        conn.close()
        print(f"[HILO] Conexión cerrada con {addr}")

def servidor_tcp_hilos():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(("127.0.0.1", 5000))
    servidor.listen(5)
    print("[SERVIDOR] Escuchando en 127.0.0.1:5000")

    while True:
        conn, addr = servidor.accept()
        print(f"[SERVIDOR] Conexión recibida de {addr}")
        hilo = threading.Thread(target=manejar_cliente, args=(conn, addr))
        hilo.start()

servidor_tcp_hilos()
