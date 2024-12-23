import socket
def cliente_tcp():
    # Solicitar al usuario la dirección IP y el puerto del servidor
    ipServidor = input("Introduce la dirección IP del servidor: ")
    puertoServidor = int(input("Introduce el puerto del servidor: "))
    # Crear socket
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Conectar al servidor con la dirección IP y puerto proporcionados
        c.connect((ipServidor, puertoServidor))
        print(f"[CLIENTE] Conectado al servidor {ipServidor}:{puertoServidor}.")

        # Recibir mensaje del servidor
        msg = c.recv(1024)
        print("[CLIENTE] Mensaje del servidor:", msg.decode())

        # Enviar una respuesta al servidor
        respuesta = "Hola servidor, aquí el cliente!"
        c.send(respuesta.encode())

        # Recibir la respuesta modificada del servidor
        msg = c.recv(1024)
        print("[CLIENTE] Mensaje del servidor:", msg.decode())

    except socket.error as e:
        print(f"[CLIENTE] Error al conectar o comunicar con el servidor: {e}")
    except Exception as e:
        print(f"[CLIENTE] Ocurrió un error inesperado: {e}")
    finally:
        # Cerrar el socket
        c.close()
        print("[CLIENTE] Conexión cerrada.")


cliente_tcp()
